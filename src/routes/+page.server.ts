import { templates } from '$src/store';
import { templatesUrl } from '$src/constants';

const makeCategories = (templates) => {
  // Get categories from templates
  const categories = templates.reduce((acc, { categories: templateCategories }) => {
    (templateCategories || []).forEach((category) => {
      acc[category] = (acc[category] || 0) + 1;
    });
    return acc;
  }, {});

  // Sort categories by count, and remove categories with only 1 template
  const sortedCategories = Object.fromEntries(
    Object.entries(categories)
      .filter(([, value]) => value > 3)
      .sort(([, a], [, b]) => b - a)
  );

  return sortedCategories;
};


export const load = async () => {
  const data = await fetch(templatesUrl).then((res) => res.json());
  templates.set(data.templates);
  
  return {
    templates: data.templates,
    categories: makeCategories(data.templates),
  }
};