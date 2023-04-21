import { get } from 'svelte/store';

import { templatesUrl } from '$src/constants';
import { templates } from '$src/store';

export const load = async () => {
  if (get(templates) && get(templates).length > 0) {
    return {
      templates: get(templates),
    }
  } else {
    const data = await fetch(templatesUrl).then((res) => res.json());
    templates.set(data.templates);    
    return {
      templates: data.templates,
    }
  }
};
