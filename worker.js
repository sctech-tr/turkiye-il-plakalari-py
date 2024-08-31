addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  if (request.method === 'GET' && request.url.endsWith('/cities')) {
    const cities = [
      { city: "Adana (01)" },

      { city: "Adiyaman (02)" },

      { city: "Afyonkarahisar (03)" },

      { city: "Agri (04)" },
  
      { city: "Amasya (05)" },
  
      { city: "Ankara (06)" },
  
      { city: "Antalya (07)" },
  
      { city: "Artvin (08)" },
  
      { city: "Aydin (09)" },
  
      { city: "Balikesir (10)" },
  
      { city: "Bilecik (11)" },
  
      { city: "Bingol (12)" },
  
      { city: "Bitlis (13)" },
  
      { city: "Bolu (14)" },
  
      { city: "Burdur (15)" },
  
      { city: "Bursa (16)" },
  
      { city: "Canakkale (17)" },
  
      { city: "Cankiri (18)" },
  
      { city: "Corum (19)" },
  
      { city: "Denizli (20)" },
  
      { city: "Diyarbakir (21)" },
  
      { city: "Edirne (22)" },
  
      { city: "Elazig (23)" },
  
      { city: "Erzincan (24)" },
  
      { city: "Erzurum (25)" },
  
      { city: "Eskisehir (26)" },
  
      { city: "Gaziantep (27)" },
  
      { city: "Giresun (28)" },
  
      { city: "Gumushane (29)" },
  
      { city: "Hakkari (30)" },
  
      { city: "Hatay (31)" },
  
      { city: "Isparta (32)" },
  
      { city: "Mersin (33)" },
  
      { city: "Istanbul (34)" },
  
      { city: "Izmir (35)" },
  
      { city: "Kars (36)" },
  
      { city: "Kastamonu (37)" },
  
      { city: "Kayseri (38)" },
  
      { city: "Kirklareli (39)" },
  
      { city: "Kirsehir (40)" },
  
      { city: "Kocaeli (41)" },
  
      { city: "Konya (42)" },
  
      { city: "Kutahya (43)" },
  
      { city: "Malatya (44)" },
  
      { city: "Manisa (45)" },
  
      { city: "Kahramanmaras (46)" },
  
      { city: "Mardin (47)" },
  
      { city: "Mugla (48)" },
  
      { city: "Mus (49)" },
  
      { city: "Nevsehir (50)" },
  
      { city: "Nigde (51)" },
  
      { city: "Ordu (52)" },
  
      { city: "Rize (53)" },
  
      { city: "Sakarya (54)" },
  
      { city: "Samsun (55)" },
  
      { city: "Siirt (56)" },
  
      { city: "Sinop (57)" },
  
      { city: "Sivas (58)" },
  
      { city: "Tekirdag (59)" },
  
      { city: "Tokat (60)" },
  
      { city: "Trabzon (61)" },
  
      { city: "Tunceli (62)" },
  
      { city: "Sanliurfa (63)" },
  
      { city: "Usak (64)" },
  
      { city: "Van (65)" },
  
      { city: "Yozgat (66)" },
  
      { city: "Zonguldak (67)" },
  
      { city: "Aksaray (68)" },
  
      { city: "Bayburt (69)" },
  
      { city: "Karaman (70)" },
  
      { city: "Kirikkale (71)" },
  
      { city: "Batman (72)" },
  
      { city: "Sirnak (73)" },
  
      { city: "Bartin (74)" },
  
      { city: "Ardahan (75)" },
  
      { city: "Igdir (76)" },
  
      { city: "Yalova (77)" },
  
      { city: "Karabuk (78)" },
  
      { city: "Kilis (79)" },
  
      { city: "Osmaniye (80)" },
  
      { city: "Duzce (81)" }
    ];

    const responseBody = cities.map(city => `${city.city}\n`).join('');

    return new Response(responseBody, {
      headers: { 'Content-Type': 'text/plain' }
    });
  } else {
    return new Response('Not found', { status: 404 });
  }
}
