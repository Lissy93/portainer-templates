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

<svelte:head>
  <title>Portainer Templates</title>
  <meta name="description" content="A community-driven library of 1-click self-hosted apps" />
  <meta property="og:title" content="Portainer Templates" />
  <meta property="og:description" content="A community-driven library of 1-click self-hosted apps" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{import.meta.env.VITE_PUBLIC_BASE_URL}/" />
  <meta property="og:image" content="{import.meta.env.VITE_PUBLIC_BASE_URL}/banner.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Portainer Templates" />
  <meta name="twitter:description" content="A community-driven library of 1-click self-hosted apps" />
  <meta name="twitter:image" content="{import.meta.env.VITE_PUBLIC_BASE_URL}/banner.png" />
  <link rel="canonical" href="{import.meta.env.VITE_PUBLIC_BASE_URL}" />
  <meta name="theme-color" content="#0ba5ec" />
</svelte:head>

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