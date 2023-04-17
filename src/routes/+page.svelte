<script lang="ts">
  import Hero from '$lib/Hero.svelte';
  import ListFilter from '$lib/ListFilter.svelte';
  import Categories from '$lib/Categories.svelte';
  import SearchSummary from '$lib/SearchSummary.svelte';
  import Templates from '$lib/TemplateList.svelte';
  import NoResults from '$lib/NoResults.svelte';
  import Footer from '$lib/Footer.svelte';

  export let data;

  let searchTerm = '';

  let selectedCategories: string[] = [];
  
  $: filteredTemplates = data.templates.filter((template: any) => {
    const compareStr = (str1: string, str2: string) =>
      (str1 || '').toLowerCase().includes(str2.toLowerCase());

    if (selectedCategories.length) {
      const templateCategories = template.categories || [];
      const hasSelectedCategory = selectedCategories.some((cat) =>
        templateCategories.includes(cat)
      );
      if (!hasSelectedCategory) return false;
    }
    return (
      compareStr(template.title, searchTerm) ||
      compareStr(template.description, searchTerm) ||
      compareStr((template.categories || []).join(''), searchTerm)
    );
  });

  const toggleCategory = (category: string) => {
    if (selectedCategories.includes(category)) {
      selectedCategories = selectedCategories.filter((cat) => cat !== category);
    } else {
      selectedCategories = [...selectedCategories, category];
    }
  };

  const clearSearch = () => {
    searchTerm = '';
    selectedCategories = [];
  }
</script>

<!-- Main title, and CTA buttons -->
<Hero />

<!-- Search bar, and Templates sub-title -->
<ListFilter bind:searchTerm={searchTerm} />

<!-- List of categories to filter by -->
<Categories
  categories={data.categories}
  selectedCategories={selectedCategories}
  toggleCategory={toggleCategory}
/>

<!-- Text showing num results, and users search term + filters  -->
<SearchSummary
  searchTerm={searchTerm}
  selectedCategories={selectedCategories}
  clearSearch={clearSearch}
  numResults={filteredTemplates.length}
  totalResults={data.templates.length}
/>

<!-- List of available templates (filtered, if needed) -->
<Templates templates={filteredTemplates} />

<!-- If there are no templates matching search term, show lil message -->
{#if !filteredTemplates.length}
  <NoResults />
{/if}

<!-- Footer showing license and source code links -->
<Footer />

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