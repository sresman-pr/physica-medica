import { renderers } from './renderers.mjs';
import { c as createExports, s as serverEntrypointModule } from './chunks/_@astrojs-ssr-adapter_Cm6ddatS.mjs';
import { manifest } from './manifest_pQcdXqF0.mjs';

const serverIslandMap = new Map();;

const _page0 = () => import('./pages/_image.astro.mjs');
const _page1 = () => import('./pages/about.astro.mjs');
const _page2 = () => import('./pages/api/keystatic/_---params_.astro.mjs');
const _page3 = () => import('./pages/blog/_slug_.astro.mjs');
const _page4 = () => import('./pages/blog.astro.mjs');
const _page5 = () => import('./pages/contact.astro.mjs');
const _page6 = () => import('./pages/insurance.astro.mjs');
const _page7 = () => import('./pages/keystatic/_---params_.astro.mjs');
const _page8 = () => import('./pages/reviews.astro.mjs');
const _page9 = () => import('./pages/schedule.astro.mjs');
const _page10 = () => import('./pages/services/pancafit-class.astro.mjs');
const _page11 = () => import('./pages/services/personal-training.astro.mjs');
const _page12 = () => import('./pages/services/pregnancy-physical-therapy.astro.mjs');
const _page13 = () => import('./pages/services/scoliosis.astro.mjs');
const _page14 = () => import('./pages/services/specialty-techniques/dry-needling-cupping.astro.mjs');
const _page15 = () => import('./pages/services/specialty-techniques/trigger-point-therapy.astro.mjs');
const _page16 = () => import('./pages/services/specialty-techniques.astro.mjs');
const _page17 = () => import('./pages/services.astro.mjs');
const _page18 = () => import('./pages/wim-hof-method.astro.mjs');
const _page19 = () => import('./pages/index.astro.mjs');
const pageMap = new Map([
    ["node_modules/astro/dist/assets/endpoint/generic.js", _page0],
    ["src/pages/about.astro", _page1],
    ["node_modules/@keystatic/astro/internal/keystatic-api.js", _page2],
    ["src/pages/blog/[slug].astro", _page3],
    ["src/pages/blog/index.astro", _page4],
    ["src/pages/contact.astro", _page5],
    ["src/pages/insurance.astro", _page6],
    ["node_modules/@keystatic/astro/internal/keystatic-astro-page.astro", _page7],
    ["src/pages/reviews.astro", _page8],
    ["src/pages/schedule.astro", _page9],
    ["src/pages/services/pancafit-class.astro", _page10],
    ["src/pages/services/personal-training.astro", _page11],
    ["src/pages/services/pregnancy-physical-therapy.astro", _page12],
    ["src/pages/services/scoliosis.astro", _page13],
    ["src/pages/services/specialty-techniques/dry-needling-cupping.astro", _page14],
    ["src/pages/services/specialty-techniques/trigger-point-therapy.astro", _page15],
    ["src/pages/services/specialty-techniques/index.astro", _page16],
    ["src/pages/services/index.astro", _page17],
    ["src/pages/wim-hof-method.astro", _page18],
    ["src/pages/index.astro", _page19]
]);

const _manifest = Object.assign(manifest, {
    pageMap,
    serverIslandMap,
    renderers,
    actions: () => import('./noop-entrypoint.mjs'),
    middleware: () => import('./_noop-middleware.mjs')
});
const _args = {
    "middlewareSecret": "54887329-148c-4c0f-83fe-3e8863245585",
    "skewProtection": false
};
const _exports = createExports(_manifest, _args);
const __astrojsSsrVirtualEntry = _exports.default;
const _start = 'start';
if (Object.prototype.hasOwnProperty.call(serverEntrypointModule, _start)) ;

export { __astrojsSsrVirtualEntry as default, pageMap };
