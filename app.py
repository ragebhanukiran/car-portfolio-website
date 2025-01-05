from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

URLs = {
    "Suzuki": "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=208affa4943c9341f287ccecdcb1c579&lang_code=en&regionId=&otherinfo=all&slug=maruti-suzuki&url=%2Fmaruti-suzuki-cars&loginUserId=&devicePlatform=web",
    "Tata": "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Tata&url=%2Fcars%2FTata&loginUserId=&devicePlatform=wap",
    "Hyundai": "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Hyundai&url=%2Fcars%2FHyundai&loginUserId=&devicePlatform=wap",
    "Mahindra": "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Mahindra&url=%2Fcars%2FMahindra&loginUserId=&devicePlatform=wap",
    "Kia": "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Kia&url=%2Fcars%2FKia&loginUserId=&devicePlatform=wap",
    "Toyota" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=toyota&url=%2Ftoyota-cars&loginUserId=&devicePlatform=web",
    "Honda" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Honda&url=%2Fcars%2FHonda&loginUserId=&devicePlatform=web",
    "MG" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=MG&url=%2Fcars%2FMG&loginUserId=&devicePlatform=web",
    "Skoda":"https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Skoda&url=%2Fcars%2FSkoda&loginUserId=&devicePlatform=web",
    "Jeep":"https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Jeep&url=%2Fcars%2FJeep&loginUserId=&devicePlatform=web",
    "Renault":"https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Renault&url=%2Fcars%2FRenault&loginUserId=&devicePlatform=wap",
    "Nissan": "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Nissan&url=%2Fcars%2FNissan&loginUserId=&devicePlatform=wap",
    "Volkswagen" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Volkswagen&url=%2Fcars%2FVolkswagen&loginUserId=&devicePlatform=wap",
    "Citreon" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Citroen&url=%2Fcars%2FCitroen&loginUserId=&devicePlatform=wap",
    "Aston Martin":"https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Aston_Martin&url=%2Fcars%2FAston_Martin&loginUserId=&devicePlatform=wap",
    "Audi" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Audi&url=%2Fcars%2FAudi&loginUserId=&devicePlatform=wap",
    "Bajaj" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Bajaj&url=%2Fcars%2FBajaj&loginUserId=&devicePlatform=wap",
    "Bentley" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Bentley&url=%2Fcars%2FBentley&loginUserId=&devicePlatform=wap",
    "BMW" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=bmw&url=%2Fbmw-cars&loginUserId=&devicePlatform=wap",
    "BYD" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=BYD&url=%2Fcars%2FBYD&loginUserId=&devicePlatform=wap",
    "Ferrari" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Ferrari&url=%2Fcars%2FFerrari&loginUserId=&devicePlatform=wap",
    "Force" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Force&url=%2Fcars%2FForce&loginUserId=&devicePlatform=wap",
    "Isuzu" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Isuzu&url=%2Fcars%2FIsuzu&loginUserId=&devicePlatform=wap",
    "Jaguar" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Jaguar&url=%2Fcars%2FJaguar&loginUserId=&devicePlatform=wap",
    "Lamborghini" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Lamborghini&url=%2Fcars%2FLamborghini&loginUserId=&devicePlatform=wap",
    "Land Rover" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Land_Rover&url=%2Fcars%2FLand_Rover&loginUserId=&devicePlatform=wap",
    "Lexus" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Lexus&url=%2Fcars%2FLexus&loginUserId=&devicePlatform=wap",
    "Lotus" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Lotus&url=%2Fcars%2FLotus&loginUserId=&devicePlatform=wap",
    "Maserati" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Maserati&url=%2Fcars%2FMaserati&loginUserId=&devicePlatform=wap",
    "MCLaren" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Mclaren&url=%2Fcars%2FMclaren&loginUserId=&devicePlatform=wap",
    "Mercedes" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Mercedes-Benz&url=%2Fcars%2FMercedes-Benz&loginUserId=&devicePlatform=wap",
    "Mini":"https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Mini&url=%2Fcars%2FMini&loginUserId=&devicePlatform=wap",
    "PMV" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=PMV&url=%2Fcars%2FPMV&loginUserId=&devicePlatform=wap",
    "Porsche" :"https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=porsche&url=%2Fporsche-cars&loginUserId=&devicePlatform=wap",
    "Pravaig" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Pravaig&url=%2Fcars%2FPravaig&loginUserId=&devicePlatform=wap",
    "Rolls Royce" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Rolls-Royce&url=%2Fcars%2FRolls-Royce&loginUserId=&devicePlatform=wap",
    "Strom Motors" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Strom_Motors&url=%2Fcars%2FStrom_Motors&loginUserId=&devicePlatform=wap",
    "Volvo" : "https://www.cardekho.com/api/v1/brand/models?_format=json&business_unit=car&country_code=in&withUpcoming=true&isFtc=false&cityId=51&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=dff5fb4a8f004a28172adb6db94e1edb&lang_code=en&regionId=&otherinfo=all&slug=Volvo&url=%2Fcars%2FVolvo&loginUserId=&devicePlatform=wap"
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*'
}

@app.route('/')
def landing_page():
    return render_template('index.html', companies=URLs.keys())

@app.route('/discover/<company>')
def discover(company):
    if company not in URLs:
        return "Company not found", 404

    api_url = URLs[company]
    response = requests.get(api_url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        car_models = [
            {
                'id': car['id'],
                'name': car['name'],
                'image': car.get('image', ''),
                'price': car.get('priceRange', 'N/A'),
                'engine': car.get('engine', 'N/A'),
                'mileage': car.get('mileage', 'N/A'),
                'seatingCapacity': car.get('seatingCapacity', 'N/A'),
                'fuelType': car.get('fuelType', 'N/A'),
                'transmissionType': car.get('transmissionType', 'N/A'),
                'power': car.get('power', 'N/A'),
                'priceRange': car.get('priceRange', 'N/A')
            }
            for car in data.get('data', {}).get('carModels', [])
        ]

        return render_template('company.html', car_models=car_models, company=company.capitalize())
    else:
        return "Error fetching car data", 500

@app.route('/explore')
def explore_page():
    return render_template('explore.html', companies=URLs.keys())

@app.route('/compare', methods=['GET', 'POST'])
def comparator():
    car_data = []

    # Fetch car data for each brand
    for brand, url in URLs.items():
        try:
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                data = response.json()
                car_models = [
                    {
                        'id': car['id'],
                        'name': car['name'],
                        'brand': brand,
                        'image': car.get('image', ''),
                        'price': car.get('priceRange', 'N/A'),
                        'engine': car.get('engine', 'N/A'),
                        'mileage': car.get('mileage', 'N/A'),
                        'seatingCapacity': car.get('seatingCapacity', 'N/A'),
                        'fuelType': car.get('fuelType', 'N/A'),
                        'transmissionType': car.get('transmissionType', 'N/A'),
                        'power': car.get('power', 'N/A'),
                        'avgRating': car.get('avgRating', 'N/A'),
                        'reviewCount': car.get('reviewCount', 'N/A')
                    }
                    for car in data.get('data', {}).get('carModels', [])
                ]
                car_data.extend(car_models)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {brand}: {e}")

    # Get selected cars from the form
    if request.method == 'POST':
        selected_cars = request.form.getlist('selectedCars')

        # Filter the selected cars from car_data
        comparison_table = [car for car in car_data if str(car['id']) in selected_cars]

        if not comparison_table:
            return render_template('comparator.html', car_data=car_data, error="Please select at least one car to compare.")

        # Show comparison table
        return render_template('comparator.html', car_data=car_data, comparison_table=comparison_table, show_comparison=True)

    # If GET request, just render the page without comparison table
    return render_template('comparator.html', car_data=car_data)

if __name__ == '__main__':
    app.run(debug=True)
