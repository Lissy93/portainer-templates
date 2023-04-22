// See how the options work here: https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API
let options = {
  root: null,
  rootMargin: "0px",
  threshold: 0
}

export const lazyLoad = (image: any, src: string) => {
  const loaded = () => {
    image.classList.remove("loading");
    image.style.opacity = "1";
  };
  const observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        image.src = src;
        if (image.complete) {
          loaded();
        } else {
          image.addEventListener("load", loaded);
        }
      }
    },
    options
  );
  observer.observe(image);

  return {
    destroy() {
      observer.disconnect();
      image.removeEventListener("load", loaded);
    },
  };
};