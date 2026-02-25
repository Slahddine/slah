// Student Grade Manager — app.js

const PASSING_GRADE = 10; // out of 20
const STORAGE_KEY = 'grade_manager_students';

let students = loadFromStorage();

// ---------- Storage ----------
function loadFromStorage() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch {
    return [];
  }
}

function saveToStorage() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(students));
}

// ---------- Calculations ----------
function calcAverage(grades) {
  const sum = grades.reduce((acc, g) => acc + g, 0);
  return +(sum / grades.length).toFixed(2);
}

function isPassing(avg) {
  return avg >= PASSING_GRADE;
}

// ---------- Render ----------
function render() {
  const tbody = document.getElementById('tableBody');
  const emptyRow = document.getElementById('emptyRow');
  const statsSection = document.getElementById('statsSection');
  const clearAllBtn = document.getElementById('clearAllBtn');

  // Remove existing dynamic rows
  tbody.querySelectorAll('tr.student-row').forEach(r => r.remove());

  if (students.length === 0) {
    emptyRow.style.display = '';
    statsSection.style.display = 'none';
    clearAllBtn.style.display = 'none';
    return;
  }

  emptyRow.style.display = 'none';
  statsSection.style.display = '';
  clearAllBtn.style.display = '';

  students.forEach((s, index) => {
    const passing = isPassing(s.average);
    const row = document.createElement('tr');
    row.className = 'student-row';
    row.innerHTML = `
      <td>${index + 1}</td>
      <td><strong>${escapeHtml(s.name)}</strong></td>
      <td>${s.grades.math}</td>
      <td>${s.grades.physics}</td>
      <td>${s.grades.french}</td>
      <td>${s.grades.science}</td>
      <td><strong>${s.average}</strong></td>
      <td>
        <span class="badge ${passing ? 'badge-success' : 'badge-danger'}">
          ${passing ? '✅ Admis' : '❌ Recalé'}
        </span>
      </td>
      <td>
        <button class="delete-btn" onclick="deleteStudent(${index})" title="Supprimer">🗑️</button>
      </td>
    `;
    tbody.appendChild(row);
  });

  renderStats();
}

function renderStats() {
  const total = students.length;
  const passed = students.filter(s => isPassing(s.average)).length;
  const failed = total - passed;
  const classAvg = total > 0
    ? +(students.reduce((acc, s) => acc + s.average, 0) / total).toFixed(2)
    : 0;

  document.getElementById('statTotal').textContent = total;
  document.getElementById('statPassed').textContent = passed;
  document.getElementById('statFailed').textContent = failed;
  document.getElementById('statAvg').textContent = total > 0 ? classAvg : '-';
}

// ---------- Actions ----------
function addStudent(name, grades) {
  const average = calcAverage(Object.values(grades));
  students.push({ name, grades, average });
  saveToStorage();
  render();
}

function deleteStudent(index) {
  if (confirm(`Supprimer l'étudiant "${students[index].name}" ?`)) {
    students.splice(index, 1);
    saveToStorage();
    render();
  }
}

function clearAll() {
  if (confirm('Supprimer tous les étudiants ?')) {
    students = [];
    saveToStorage();
    render();
  }
}

// ---------- Form ----------
document.getElementById('studentForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('studentName').value.trim();
  const math = parseFloat(document.getElementById('math').value);
  const physics = parseFloat(document.getElementById('physics').value);
  const french = parseFloat(document.getElementById('french').value);
  const science = parseFloat(document.getElementById('science').value);

  if (!name) {
    alert('Veuillez entrer le nom de l\'étudiant.');
    return;
  }

  addStudent(name, { math, physics, french, science });
  this.reset();
  document.getElementById('studentName').focus();
});

// ---------- Utilities ----------
function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ---------- Init ----------
render();
