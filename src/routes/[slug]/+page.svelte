<script lang="ts">

  import { page } from '$app/stores';

  import ServiceStats from '$lib/ServiceStats.svelte';
  import TemplateNotFound from '$lib/TemplateNotFound.svelte';
  import DockerStats from '$lib/DockerStats.svelte';
  import MdContent from '$lib/MdContent.svelte';
  import InstallationInstructions from '$lib/InstallationInstructions.svelte';

  import type { Template, Service, DockerHubResponse } from '$src/Types';

  const urlSlug = $page.params.slug;
  const template = $page.data.template as Template;
  const dockerStats = $page.data.dockerStats as DockerHubResponse;
  const services = $page.data.services as Service[];
  const serviceDockerStats = $page.data.serviceDockerStats as DockerHubResponse[] || null;

  const makeMultiDoc = (services: Service[]) => {
    return services.map((s) => {
      return s?.dockerStats?.full_description ? {
        name: s.name,
        description: s.dockerStats.description,
        content: s.dockerStats.full_description,
        visible: false,
      } : null;
    }).filter((thingy) => thingy !== null);
  };

</script>

{#if template}
  <section class="summary-section">
    <h1>
      {#if template.logo} <img src={template.logo} /> {/if}
      {template.title}
    </h1>
    {#if template.categories || template.category }
      <p class="tags">
        {#each (template.categories || template.category || []) as tag}
          <span>{tag}</span>
        {/each}
      </p>
    {/if}
    <div class="content">
      <div class="left">
        <p class="description">{template.description}</p>
        {#await template then returnedTemplate}
          {#if dockerStats && dockerStats.name}
          <DockerStats info={dockerStats} />
          {/if}
        {/await}
      </div>
      <ServiceStats template={template} />
    </div>
  </section>

  {#await services then returnedServices}
  {#if returnedServices && returnedServices.length > 0}
    <section class="service-section">
      <h2>Services</h2>
      <div class="service-list">
        {#each returnedServices as service}
          <div class="service-each">
          <h3>{service.name}</h3>  
          <div class="service-data">
            <ServiceStats template={service} />
            {#if service.dockerStats && service.dockerStats.name}
              <DockerStats info={service.dockerStats} />
            {/if}
          </div>
        </div>
        {/each}
      </div>
    </section>
  {/if}
  {/await}

  <InstallationInstructions portainerTemplate={template} portainerServices={services || null} />

  {#if dockerStats?.full_description}
    <MdContent content={dockerStats.full_description} />
  {:else if services.length > 0}
    <MdContent multiContent={makeMultiDoc(services)} />
  {/if}

{:else}
  <TemplateNotFound templateName={urlSlug} />
{/if}


<style lang="scss">
  section {
    max-width: 1000px;
    margin: 1rem auto;
  }
  .summary-section {
    background: var(--card);
    border-radius: 6px;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    h1 {
      font-size: 4rem;
      margin: 0;
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    img {
      border-radius: 6px;
      width: 64px;
      max-height: 64px;
    }
    .tags {
      display: flex;
      margin: 0;
      span {
        &:before {
          content: '#';
          opacity: 0.5;
        }
        &:not(:last-child)::after {
          content: ',';
          margin-right: 0.5rem;
        }
      }
    }
  }

  .content {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: space-between;
    margin-top: 1rem;
    .left {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    p.description {
      background: var(--card-2);
      padding: 1rem;
      border-radius: 6px;
      margin: 0;
    }
  }

  .service-section {
    background: var(--card);
    border-radius: 6px; 
    padding: 1rem;
    h2 {
      margin: 0;
      font-size: 2rem;
    }
    .service-list {
      display: flex;
      gap: 2rem;
      flex-wrap: wrap;
      h3 {
        margin: 0.5rem 0;
        font-weight: 400;
        font-size: 2rem;
      }
      .service-each {
        .service-data {
          display: flex;
          gap: 1rem;
        }
      }
    }
  }
</style>
