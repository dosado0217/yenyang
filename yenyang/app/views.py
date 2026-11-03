
from django.shortcuts import render


# ============================================================
# YENYANG TRANSPORTATION SERVICES & ISLAND ADVENTURES
# CUSTOMER SHOWCASE - MOCK DATA ONLY
# ============================================================


def dashboard(request):

    # ========================================================
    # VEHICLE FLEET
    # ========================================================

    vehicles = [

        # ---------------- 4-SEATERS ----------------

        {
            "id": "sedan-01",
            "name": "Toyota Vios",
            "category": "4-seaters",
            "type": "Premium Sedan",
            "image": "img/fleet/toyota-vios.jpg",
            "passengers": "4 Passengers",
            "luggage": "2 Medium Bags",
            "transmission": "Automatic",
            "rate": "₱2,500",
            "rate_unit": "/ day",
            "rate_note": "Sample rate",
            "with_chauffeur": True,
            "full_ac": True,
            "description": "A comfortable and practical ride for city tours, airport transfers, and small families.",
            "featured": True,
        },

        # ---------------- 7-SEATERS ----------------

        {
            "id": "suv-01",
            "name": "Toyota Innova",
            "category": "7-seaters",
            "type": "Family MPV",
            "image": "img/fleet/toyota-innova.jpg",
            "passengers": "7 Passengers",
            "luggage": "3 Medium Bags",
            "transmission": "Automatic",
            "rate": "₱3,500",
            "rate_unit": "/ day",
            "rate_note": "Sample rate",
            "with_chauffeur": True,
            "full_ac": True,
            "description": "Ideal for family vacations, comfortable sightseeing, and private Cebu tours.",
            "featured": True,
        },

        # ---------------- BIG VANS ----------------

        {
            "id": "van-01",
            "name": "Toyota HiAce",
            "category": "vans",
            "type": "Premium Passenger Van",
            "image": "img/fleet/toyota-hiace.jpg",
            "passengers": "12-15 Passengers",
            "luggage": "Large Luggage Capacity",
            "transmission": "Manual / Automatic",
            "rate": "₱5,500",
            "rate_unit": "/ day",
            "rate_note": "Sample rate",
            "with_chauffeur": True,
            "full_ac": True,
            "description": "Perfect for barkada trips, corporate outings, airport transfers, and island adventures.",
            "featured": True,
        },

        # ---------------- MINI BUSES ----------------

        {
            "id": "bus-01",
            "name": "Toyota Coaster",
            "category": "mini-buses",
            "type": "Mini Bus",
            "image": "img/fleet/coaster.jpg",
            "passengers": "22-26 Passengers",
            "luggage": "Large Luggage Capacity",
            "transmission": "Manual",
            "rate": "₱9,000",
            "rate_unit": "/ day",
            "rate_note": "Sample rate",
            "with_chauffeur": True,
            "full_ac": True,
            "description": "An excellent choice for company outings, large family gatherings, and group excursions.",
            "featured": True,
        },

    ]


    # ========================================================
    # VEHICLE CATEGORY TABS
    # ========================================================

    vehicle_categories = [

        {
            "id": "all",
            "name": "All Vehicles",
        },

        {
            "id": "4-seaters",
            "name": "4-Seaters",
        },

        {
            "id": "7-seaters",
            "name": "7-Seaters",
        },

        {
            "id": "vans",
            "name": "Big Vans",
        },

        {
            "id": "mini-buses",
            "name": "Mini Buses",
        },

    ]


    # ========================================================
    # CEBU TOUR DESTINATIONS
    # ========================================================

    destinations = [

        {
            "id": "oslob",
            "name": "Oslob Whale Sharks",
            "location": "Oslob, South Cebu",
            "image": "img/destinations/oslob.jpg",
            "tagline": "Meet the Gentle Giants",
            "description": "Experience the unforgettable opportunity to see whale sharks in the waters of Oslob.",
            "duration": "Full-Day Adventure",
            "icon": "bi-water",
        },

        {
            "id": "kawasan",
            "name": "Kawasan Canyoneering",
            "location": "Badian, South Cebu",
            "image": "img/destinations/kawasan.jpg",
            "tagline": "Chase the Adventure",
            "description": "Explore turquoise waterfalls, natural pools, river trails, and thrilling canyon adventures.",
            "duration": "Full-Day Adventure",
            "icon": "bi-water",
        },

        {
            "id": "moalboal",
            "name": "Moalboal Sardine Run",
            "location": "Moalboal, Cebu",
            "image": "img/destinations/moalboal.jpg",
            "tagline": "Dive Into Wonder",
            "description": "Discover the famous sardine run and experience the incredible marine life of Moalboal.",
            "duration": "Full-Day Adventure",
            "icon": "bi-water",
        },

        {
            "id": "bantayan",
            "name": "Bantayan Island",
            "location": "Bantayan, North Cebu",
            "image": "img/destinations/bantayan.jpg",
            "tagline": "Escape to Paradise",
            "description": "Enjoy beautiful white-sand beaches, crystal-clear waters, and a relaxing island atmosphere.",
            "duration": "Multi-Day Adventure",
            "icon": "bi-umbrella",
        },

        {
            "id": "cebu-city",
            "name": "Cebu City Heritage Tour",
            "location": "Cebu City",
            "image": "img/destinations/cebu-city.jpg",
            "tagline": "Discover Cebu's History",
            "description": "Visit historical landmarks, cultural attractions, and iconic destinations around Cebu City.",
            "duration": "Half-Day / Full-Day",
            "icon": "bi-building",
        },

    ]


    # ========================================================
    # FEATURED TOUR PACKAGES
    # ========================================================

    tour_packages = [

        {
            "id": "tour-01",
            "name": "Oslob Whale Shark Adventure",
            "destination": "oslob",
            "image": "img/packages/oslob-package.jpg",
            "duration": "Full Day",
            "package_type": "Marine Adventure",
            "price": "₱2,500",
            "price_unit": "/ person",
            "price_note": "Sample price",
            "highlights": [
                "Oslob Whale Shark Experience",
                "South Cebu Scenic Drive",
                "Private Transportation",
            ],
            "featured": True,
        },

        {
            "id": "tour-02",
            "name": "Kawasan Canyoneering Adventure",
            "destination": "kawasan",
            "image": "img/packages/kawasan-package.jpg",
            "duration": "Full Day",
            "package_type": "Adventure Tour",
            "price": "₱2,800",
            "price_unit": "/ person",
            "price_note": "Sample price",
            "highlights": [
                "Canyoneering Experience",
                "Waterfall Adventure",
                "South Cebu Transportation",
            ],
            "featured": True,
        },

        {
            "id": "tour-03",
            "name": "Moalboal Island Experience",
            "destination": "moalboal",
            "image": "img/packages/moalboal-package.jpg",
            "duration": "Full Day",
            "package_type": "Island Adventure",
            "price": "₱2,200",
            "price_unit": "/ person",
            "price_note": "Sample price",
            "highlights": [
                "Sardine Run Experience",
                "Marine Life Exploration",
                "Private Transportation",
            ],
            "featured": True,
        },

        {
            "id": "tour-04",
            "name": "Bantayan Island Escape",
            "destination": "bantayan",
            "image": "img/packages/bantayan-package.jpg",
            "duration": "2 Days / 1 Night",
            "package_type": "Island Getaway",
            "price": "₱5,500",
            "price_unit": "/ person",
            "price_note": "Sample price",
            "highlights": [
                "White-Sand Beaches",
                "Island Exploration",
                "Relaxing Beach Experience",
            ],
            "featured": False,
        },

        {
            "id": "tour-05",
            "name": "Cebu City Heritage Discovery",
            "destination": "cebu-city",
            "image": "img/packages/cebu-city-package.jpg",
            "duration": "Half Day",
            "package_type": "Cultural Tour",
            "price": "₱1,800",
            "price_unit": "/ person",
            "price_note": "Sample price",
            "highlights": [
                "Historical Landmarks",
                "Cultural Attractions",
                "City Transportation",
            ],
            "featured": True,
        },

    ]


    # ========================================================
    # WHY CHOOSE YENYANG
    # ========================================================

    why_choose_yenyang = [

        {
            "icon": "bi-car-front-fill",
            "title": "Comfortable Transportation",
            "description": "Enjoy convenient transportation for your Cebu adventures.",
        },

        {
            "icon": "bi-geo-alt-fill",
            "title": "Explore Cebu",
            "description": "Discover beautiful destinations with convenient travel arrangements.",
        },

        {
            "icon": "bi-people-fill",
            "title": "Group-Friendly Options",
            "description": "Vehicle choices for couples, families, friends, and larger groups.",
        },

        {
            "icon": "bi-chat-dots-fill",
            "title": "Easy Inquiries",
            "description": "Contact us directly through WhatsApp to discuss your travel plans.",
        },

    ]


    # ========================================================
    # CUSTOMER REVIEWS
    # ========================================================

    # Keep empty until Yenyang has verified customer testimonials.
    # Do not publish invented customer reviews as genuine feedback.

    customer_reviews = []


    # ========================================================
    # HOMEPAGE CONTEXT
    # ========================================================

    context = {

        "company_name": "Yenyang Transportation Services & Island Adventures",

        "tagline": "Explore Cebu. Ride in Comfort. Adventure Without Limits.",

        "vehicles": vehicles,

        "vehicle_categories": vehicle_categories,

        "destinations": destinations,

        "tour_packages": tour_packages,

        "why_choose_yenyang": why_choose_yenyang,

        "customer_reviews": customer_reviews,

    }


    # ========================================================
    # RENDER CUSTOMER SHOWCASE
    # ========================================================

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )
