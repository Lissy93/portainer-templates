<script lang="ts">
  import Button from '$lib/Button.svelte';
  import { gitHubRepo } from '$src/constants';
</script>

<header>
  <a class="title" href="/">
    <img src="https://i.ibb.co/hMymwH0/portainer-templates-small.png" />
    <h2>Portainer Templates</h2>
  </a>
  <nav>
    <Button to="/">Home</Button>
    <Button to={gitHubRepo} icon="github">GitHub</Button>
  </nav>
</header>

<style lang="scss">
  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--card);
    padding: 0.25rem 1rem;
    flex-wrap: wrap;
    a.title {
      display: flex;
      justify-content: center;
      gap: 1rem;
      color: var(--foreground);
      text-decoration: none;
      h2 {
        margin: 0;
        font-size: 1.5rem;
        font-weight: 600;
      }
      img {
        width: 40px;
        transition: all 0.3s ease-in-out;
      }
      &:hover {
        img { transform: rotate(-5deg) scale(1.1); }
      }
    }

    nav {
      display: flex;
      gap: 1rem;
    }
    &.fixed {
      position: fixed;
      top: 0;
      width: calc(100% - 2rem);
      box-shadow: 0 3px 4px 0 var(--background);
    }
  }
</style>