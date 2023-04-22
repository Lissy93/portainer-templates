<script lang="ts">
  import { gitHubRepo } from '$src/constants'; 
  export let templateName: string;
</script>

<section>
  <h2>Template not Found 😢</h2>
  <p class="subtitle">It doesn't look like there was a templated named "<i>{templateName}</i>"</p>
  <p>
    You can try <a href="/">searching for another</a>, or if you think there's a mistake somewhere,
    please open an issue on the <a href={gitHubRepo} target="_blank">Github Repo</a>.
  </p>
  <a class="back-home" href="/">Back Home</a>
</section>

<style lang="scss">
  section {
    background: var(--card);
    padding: 1rem;
    border-radius: 6px;
    margin: 1rem auto;
    max-width: 1000px;
    transition: all 0.2s ease-in-out;
    h2 {
      margin: 0;
      font-size: 3rem;
      text-align: center;
    }
    p {
      margin: 1rem auto;
      font-size: 1.1rem;
      opacity: 0.8;
      text-align: center;
      max-width: 40rem;
      a {
        color: var(--accent);
      }
    }
    .back-home {
      background: var(--background);
      padding: 0.25rem 0.5rem;
      margin: 0 auto;
      display: block;
      width: fit-content;
      border-radius: 6px;
      border: none;
      color: var(--foreground);
      font-family: Kanit;
      font-size: 1.5rem;
      cursor: pointer;
      transition: all 0.2s ease-in-out;
      text-decoration: none;
      &:hover {
        background: var(--gradient);
        transform: scale(1.1) rotate(-1deg);
      }
    }
    
  }
</style>