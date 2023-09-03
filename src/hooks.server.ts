import { sequence } from "@sveltejs/kit/hooks";
import { handleErrorWithSentry, sentryHandle } from "@sentry/sveltekit";
import * as Sentry from '@sentry/sveltekit';

Sentry.init({
  dsn: 'https://400f8ec8eaab4315bcda4f150e04f4fc@glitch.as93.net/2',
  tracesSampleRate: 1.0,
});

export const handle = sequence(sentryHandle());

export const handleError = handleErrorWithSentry();
