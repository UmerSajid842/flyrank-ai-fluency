(() => {
  const button = document.querySelector('[data-evidence-status]');
  const output = document.querySelector('[data-evidence-output]');
  if (!button || !output) return;

  const repo = 'UmerSajid842/flyrankmlproject';
  const endpoint = `https://api.github.com/repos/${repo}`;

  const show = (message, state = 'neutral') => {
    output.hidden = false;
    output.dataset.state = state;
    output.textContent = message;
  };

  button.addEventListener('click', async () => {
    button.disabled = true;
    button.textContent = 'Checking public repository…';
    show('Loading the current public repository record…');

    try {
      const response = await fetch(endpoint, {
        headers: { Accept: 'application/vnd.github+json' }
      });
      if (!response.ok) throw new Error(`GitHub returned ${response.status}`);

      const data = await response.json();
      const updated = new Intl.DateTimeFormat(undefined, {
        dateStyle: 'medium', timeStyle: 'short'
      }).format(new Date(data.updated_at));
      const branch = data.default_branch || 'not reported';
      const visibility = data.private ? 'private' : 'public';

      show(
        `Verified live: this ${visibility} repository’s default branch is “${branch}” and GitHub reports it was last updated ${updated}. Use “Inspect the repository” above to review the source itself.`,
        'success'
      );
    } catch (error) {
      show(
        'The public repository record could not be loaded right now. You can still use the direct repository link above; please try this check again later.',
        'error'
      );
      console.error('Evidence-status check failed:', error);
    } finally {
      button.disabled = false;
      button.textContent = 'Check the live repository record';
    }
  });
})();
