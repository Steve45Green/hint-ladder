// Exercise components shared by every lesson in the workspace.
//   .quiz     multiple choice; data-answer = index of the right <button>, counting from 0
//   .predict  typed answer; data-answer = expected output (whitespace runs are ignored)
// Both reveal their .explain paragraph after an attempt.

const normalise = s => s.trim().split(/\s+/).join(' ');

function reveal(block, right) {
  block.classList.toggle('right', right);
  block.classList.toggle('wrong', !right);
  block.querySelector('.explain')?.removeAttribute('hidden');
}

document.querySelectorAll('.quiz').forEach(quiz => {
  const buttons = [...quiz.querySelectorAll('button')];
  const answer = Number(quiz.dataset.answer);
  buttons.forEach((button, i) => button.addEventListener('click', () => {
    buttons.forEach(b => { b.disabled = true; });
    buttons[answer].classList.add('correct');
    if (i !== answer) button.classList.add('chosen');
    reveal(quiz, i === answer);
  }));
});

document.querySelectorAll('.predict').forEach(block => {
  const input = block.querySelector('input');
  const check = () => reveal(block, normalise(input.value) === normalise(block.dataset.answer));
  block.querySelector('button').addEventListener('click', check);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
});
