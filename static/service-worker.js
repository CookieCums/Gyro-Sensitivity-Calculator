const CACHE_NAME = 'gyro-sensitivity-cache-v1';
const urlsToCache = [
    '/',
    '/static/style.css',
    '/static/manifest.json',
    '/static/icons/icon-192x192.png',
    '/static/icons/icon-512x512.png',
    '/static/icons/favicon.ico',
    '/static/icons/apple-touch-icon.png',
    '/static/icons/apple-touch-icon-precomposed.png',
    '/static/icons/apple-touch-icon-120x120.png',
    '/static/icons/apple-touch-icon-120x120-precomposed.png'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
    );
});

self.addEventListener('activate', event => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
