

<slot></slot>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200;400;800&display=swap');
  :global(body) {
    --background: #101828;
    --foreground: #ffffff;
    --accent: #0ba5ec;
    --card: #1d2939;
    --shadow: 1px 1px 3px 3px #0B9AEC8F;
    --gradient: linear-gradient(to right,#0B9AEC 0%,#6EDFDE 100%);
    --max-width: 1800px;
    margin: 0;
    font-family: 'Kanit', sans-serif;
    color: var(--foreground);
    background: var(--background);
  }
  :global(::selection) {
    background: var(--card);
    color: var(--accent);
  }

</style>