/** @type {{ name: string, grade: number, coeff: number }[]} */
let subjects = [];

/**
 * Returns an appreciation string and CSS class based on a grade out of 20.
 * @param {number} grade
 * @returns {{ label: string, cls: string }}
 */
function getAppreciation(grade) {
  if (grade >= 16) return { label: 'Excellent',    cls: 'app-excellent' };
  if (grade >= 14) return { label: 'Très Bien',    cls: 'app-tres-bien' };
  if (grade >= 12) return { label: 'Bien',          cls: 'app-bien' };
  if (grade >= 10) return { label: 'Assez Bien',   cls: 'app-assez-bien' };
  if (grade >= 8)  return { label: 'Passable',      cls: 'app-passable' };
  return                  { label: 'Insuffisant',   cls: 'app-insuffisant' };
}

/**
 * Computes the weighted average of all subjects.
 * @returns {number}
 */
function computeAverage() {
  const totalWeighted = subjects.reduce((sum, s) => sum + s.grade * s.coeff, 0);
  const totalCoeff    = subjects.reduce((sum, s) => sum + s.coeff, 0);
  return totalCoeff === 0 ? 0 : totalWeighted / totalCoeff;
}

/**
 * Returns the mention (honor label) for a given average.
 * @param {number} avg
 * @returns {string}
 */
function getMention(avg) {
  if (avg >= 16) return '🏆 Félicitations du jury';
  if (avg >= 14) return '🥇 Très Bien';
  if (avg >= 12) return '🥈 Bien';
  if (avg >= 10) return '🥉 Assez Bien';
  return '❌ Ajourné(e)';
}

/** Re-renders the grades table and summary section. */
function render() {
  const resultsCard = document.getElementById('resultsCard');
  const tbody       = document.getElementById('gradesBody');
  const avgEl       = document.getElementById('average');
  const mentionEl   = document.getElementById('mention');
  const resultEl    = document.getElementById('result');

  if (subjects.length === 0) {
    resultsCard.style.display = 'none';
    return;
  }

  resultsCard.style.display = 'block';
  tbody.innerHTML = '';

  subjects.forEach((s, i) => {
    const app = getAppreciation(s.grade);
    const tr  = document.createElement('tr');
    tr.innerHTML = `
      <td>${escapeHtml(s.name)}</td>
      <td><strong>${s.grade.toFixed(2)}</strong></td>
      <td>${s.coeff}</td>
      <td><span class="appreciation ${app.cls}">${app.label}</span></td>
      <td><button class="btn-delete" onclick="removeSubject(${i})" title="Supprimer">✕</button></td>
    `;
    tbody.appendChild(tr);
  });

  const avg    = computeAverage();
  const passed = avg >= 10;

  avgEl.textContent    = avg.toFixed(2) + ' / 20';
  mentionEl.textContent = getMention(avg);
  resultEl.textContent  = passed ? 'Admis(e) ✅' : 'Ajourné(e) ❌';
  resultEl.className    = 'value ' + (passed ? 'result-pass' : 'result-fail');
}

/** Adds a subject from the form inputs. */
function addSubject() {
  const nameInput  = document.getElementById('subjectName');
  const gradeInput = document.getElementById('subjectGrade');
  const coeffInput = document.getElementById('subjectCoeff');
  const errorEl    = document.getElementById('formError');

  const name  = nameInput.value.trim();
  const grade = parseFloat(gradeInput.value);
  const coeff = parseInt(coeffInput.value, 10);

  // Validation
  if (!name) {
    showError(errorEl, 'Veuillez saisir le nom de la matière.');
    return;
  }
  if (isNaN(grade) || grade < 0 || grade > 20) {
    showError(errorEl, 'La note doit être un nombre entre 0 et 20.');
    return;
  }
  if (isNaN(coeff) || coeff < 1 || coeff > 10) {
    showError(errorEl, 'Le coefficient doit être un entier entre 1 et 10.');
    return;
  }

  errorEl.classList.add('hidden');
  subjects.push({ name, grade, coeff });

  // Reset inputs
  nameInput.value  = '';
  gradeInput.value = '';
  coeffInput.value = '1';
  nameInput.focus();

  render();
}

/**
 * Removes a subject by index.
 * @param {number} index
 */
function removeSubject(index) {
  subjects.splice(index, 1);
  render();
}

/** Clears all subjects after confirmation. */
function clearAll() {
  if (subjects.length === 0) return;
  if (confirm('Voulez-vous vraiment effacer toutes les matières ?')) {
    subjects = [];
    render();
  }
}

/**
 * Displays an error message in the given element.
 * @param {HTMLElement} el
 * @param {string} msg
 */
function showError(el, msg) {
  el.textContent = msg;
  el.classList.remove('hidden');
}

/**
 * Escapes HTML special characters to prevent XSS.
 * @param {string} str
 * @returns {string}
 */
function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Allow pressing Enter in any input field to trigger addSubject
document.addEventListener('DOMContentLoaded', () => {
  ['subjectName', 'subjectGrade', 'subjectCoeff'].forEach(id => {
    document.getElementById(id).addEventListener('keydown', e => {
      if (e.key === 'Enter') addSubject();
    });
  });
});
