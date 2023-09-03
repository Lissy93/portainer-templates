import { handleErrorWithSentry, Replay } from "@sentry/sveltekit";
import * as Sentry from '@sentry/sveltekit';

Sentry.init({
  dsn: 'https://400f8ec8eaab4315bcda4f150e04f4fc@glitch.as93.net/2',
  tracesSampleRate: 1.0,
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  integrations: [new Replay()],
});

export const handleError = handleErrorWithSentry();
