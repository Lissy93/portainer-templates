<script>
    import Icon from '$lib/Icon.svelte';
</script>

<div class="hero">
  <header>
    <h1>Portainer Templates</h1>
    <p class="sub-title">The largest single collection, of ready-to-go Portainer templates</p>
  </header>

  <section class="cta">
    <a href="https://github.com/Lissy93/portainer-templates">
      <Icon name="github" width="26px" height="26px" />
      View on GitHub
    </a>
    <a href="https://github.com/Lissy93/portainer-templates">
      <Icon name="portainer" width="26px" height="26px" />
      Install on Portainer
    </a>
  </section>
</div>

<style lang="scss">
.hero {
    padding: 2rem;
    header {
    h1 {
      text-align: center;
      font-size: 4rem;
      margin: 0 auto;
      background: var(--gradient);
      background-clip: border-box;
      -moz-background-clip: text;
      -webkit-background-clip: text;
      background-clip: text;
      -moz-text-fill-color: transparent;
      -webkit-text-fill-color: transparent;
      color: transparent;
    }
    .sub-title {
      text-align: center;
      margin: 0 auto;
      font-size: 1.4rem;
      font-style: italic;
      font-weight: 200;
    }
  }

  section.cta {
    margin: 1rem auto;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
    a {
      font-size: 1.2rem;
      transition:all 0.3s ease-in-out;
      position: relative;
      border-radius: 6px;
      background: var(--background);
      background-clip: padding-box;
      padding: 0.5rem 1rem;
      cursor: pointer;
      display: flex;
      gap: 1rem;
      align-items: center;
      min-width: 13rem;
      color: var(--foreground);
      text-decoration: none;
      &::after {
        position: absolute;
        top: -4px; bottom: -4px;
        left: -4px; right: -4px;
        background: var(--gradient);
        content: '';
        z-index: -1;
        border-radius: 6px;
      }
      &:hover {
        background: var(--gradient);
        transform: scale(1.03) rotate(-0.6deg);
      }
    }
  }
}

</style>