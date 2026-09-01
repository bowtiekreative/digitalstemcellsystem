/* DigitalStemCell docs — small progressive enhancements.
   laka.js handles the menu, reveal and focus behaviour; this file only adds
   the live explorer and marks the current page in the mega menu. */
(function () {
  'use strict';

  var API = 'https://api.digitalstemcell.bowtiekreative.com';

  /* ------------------------------------------------ current page marker */
  var here = location.pathname.replace(/index\.html$/, '') || '/';
  document.querySelectorAll('.megamenu a, .toc a').forEach(function (a) {
    var href = a.getAttribute('href') || '';
    if (href === here || (here !== '/' && href !== '/' && here.indexOf(href) === 0)) {
      a.setAttribute('aria-current', 'page');
    }
  });

  /* ------------------------------------------------------- the explorer */
  var form = document.getElementById('explorer-form');
  if (!form) return;

  var out = document.getElementById('explorer-output');
  var status = document.getElementById('explorer-status');
  var urlLabel = document.getElementById('explorer-url');
  var preset = document.getElementById('explorer-preset');
  var pathInput = document.getElementById('explorer-path');
  var methodInput = document.getElementById('explorer-method');
  var bodyField = document.getElementById('explorer-body-field');
  var bodyInput = document.getElementById('explorer-body');

  var PRESETS = {
    'coordinate': { method: 'GET', path: '/v1/coordinates/LAKA-C3-I07-M08' },
    'prompts': { method: 'GET', path: '/v1/prompts?change=C2&internal=I07&limit=5' },
    'axes': { method: 'GET', path: '/v1/axes/meta-variables' },
    'grid': { method: 'GET', path: '/v1/grid?change=C4' },
    'modes': { method: 'GET', path: '/v1/modes/PREDICT' },
    'operators': { method: 'GET', path: '/v1/operators?category=Transformation' },
    'templates': { method: 'GET', path: '/v1/templates/run-laka' },
    'scoring': { method: 'GET', path: '/v1/scoring' },
    'score': {
      method: 'POST', path: '/v1/score',
      body: JSON.stringify({
        ratings: {
          outcome_contribution: 3, feasibility: 2, evidence: 2, adoption: 3,
          differentiation: 4, reversible_learning: 3, robustness: 2
        },
        hard_gates_passed: true
      }, null, 2)
    },
    'validate': {
      method: 'POST', path: '/v1/validate',
      body: JSON.stringify({ run_id: 'demo', mode: 'GENERATE' }, null, 2)
    }
  };

  function syncBodyVisibility() {
    bodyField.hidden = methodInput.value !== 'POST';
  }

  function syncUrl() {
    urlLabel.textContent = methodInput.value + ' ' + API + pathInput.value;
  }

  if (preset) {
    preset.addEventListener('change', function () {
      var p = PRESETS[preset.value];
      if (!p) return;
      methodInput.value = p.method;
      pathInput.value = p.path;
      bodyInput.value = p.body || '';
      syncBodyVisibility();
      syncUrl();
    });
  }
  methodInput.addEventListener('change', function () { syncBodyVisibility(); syncUrl(); });
  pathInput.addEventListener('input', syncUrl);
  syncBodyVisibility();
  syncUrl();

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var path = pathInput.value.trim();
    if (path.charAt(0) !== '/') {
      status.textContent = 'The path must start with a slash.';
      status.className = 'laka-error';
      return;
    }

    var opts = { method: methodInput.value, headers: { accept: 'application/json' } };
    if (methodInput.value === 'POST') {
      try {
        JSON.parse(bodyInput.value);
      } catch (err) {
        status.textContent = 'Request body is not valid JSON: ' + err.message;
        status.className = 'laka-error';
        return;
      }
      opts.headers['content-type'] = 'application/json';
      opts.body = bodyInput.value;
    }

    status.textContent = 'Requesting…';
    status.className = 'laka-hint';
    out.textContent = '';

    var started = Date.now();
    fetch(API + path, opts)
      .then(function (res) {
        return res.text().then(function (text) {
          var pretty = text;
          try { pretty = JSON.stringify(JSON.parse(text), null, 2); } catch (err) { /* keep raw */ }
          return { status: res.status, ok: res.ok, body: pretty };
        });
      })
      .then(function (r) {
        var ms = Date.now() - started;
        status.textContent = r.status + ' · ' + ms + ' ms';
        status.className = r.ok ? 'laka-hint' : 'laka-error';
        out.textContent = r.body;
      })
      .catch(function (err) {
        status.textContent = 'Request failed: ' + err.message;
        status.className = 'laka-error';
        out.textContent = '';
      });
  });
})();
