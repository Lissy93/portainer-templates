<script lang="ts">
  import { browser } from '$app/environment';
  import { page, navigating } from '$app/stores';
  import { tick } from 'svelte';
  import Header from '$lib/Header.svelte';
  import Footer from '$lib/Footer.svelte';

  let bottom = false;
  let showNav = false;
  
  const scrollVisible = (): boolean => {
    return browser ?
      document.documentElement.clientHeight >= document.documentElement.scrollHeight
      : false;
  };

  $: {
    updateFooter();
    if($navigating) updateFooter();
    showNav = !['/', '/index'].includes($page.url.pathname)
  }

  async function updateFooter() {
    await tick();
    bottom = scrollVisible();
  }
</script>

{#if showNav}
  <Header />
{/if}
<main>
  <slot></slot>
</main>
<Footer {bottom} />


<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200;400;800&display=swap');
  :global(body) {
    --background: #101828;
    --foreground: #ffffff;
    --accent: #0ba5ec;
    --card: #1d2939;
    --card-2: #192432;
    --shadow: 1px 1px 3px 3px #0B9AEC8F;
    --gradient: linear-gradient(to right,#0B9AEC 0%,#6EDFDE 100%);
    --max-width: 1800px;
    margin: 0;
    font-family: 'Kanit', sans-serif;
    color: var(--foreground);
    background: var(--background);
  }
  :global(::selection) {
    background: var(--accent);
    color: var(--background);
  }
  main {
    padding: 2rem;
  }

</style>