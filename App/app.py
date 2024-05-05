from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('cleaned.csv')

@app.route('/')
def index():
    # Get distinct values for make
    makes = df['Make'].unique().tolist()
    return render_template('index.html', makes=makes)

@app.route('/get_models', methods=['POST'])
def get_models():
    make = request.form['make']
    models = df[df['Make'] == make]['Model'].unique().tolist()
    return jsonify({'models': models})

@app.route('/get_variants', methods=['POST'])
def get_variants():
    make = request.form['make']
    model = request.form['model']
    variants = df[(df['Make'] == make) & (df['Model'] == model)]['Variant'].unique().tolist()
    return jsonify({'variants': variants})

@app.route('/results', methods=['POST'])
def results():
    make1 = request.form['make1']
    model1 = request.form['model1']
    variant1 = request.form['variant1']
    
    make2 = request.form['make2']
    model2 = request.form['model2']
    variant2 = request.form['variant2']
    
    # Filter the dataset based on selected cars
    car1 = df[(df['Make'] == make1) & (df['Model'] == model1) & (df['Variant'] == variant1)]
    car2 = df[(df['Make'] == make2) & (df['Model'] == model2) & (df['Variant'] == variant2)]
    
    # Extract data for comparison
    ex_showroom_price_data = [int(car1['Ex-Showroom_Price']), int(car2['Ex-Showroom_Price'])]
    displacement_data = [int(car1['Displacement']), int(car2['Displacement'])]
    fuel_type_data = [car1['Fuel_Type'].iloc[0], car2['Fuel_Type'].iloc[0]]
    arai_certified_mileage_data = [float(car1['ARAI_Certified_Mileage']), float(car2['ARAI_Certified_Mileage'])]
    fuel_tank_capacity_data = [float(car1['Fuel_Tank_Capacity']), float(car2['Fuel_Tank_Capacity'])]
    power_data = [float(car1['Power']), float(car2['Power'])]
    torque_data = [float(car1['Torque']), float(car2['Torque'])]
    car_type_data = [car1['Type'].iloc[0], car2['Type'].iloc[0]]
    cylinders_data = [int(car1['Cylinders']), int(car2['Cylinders'])]
    ground_clearance_data = [float(car1['Ground_Clearance']), float(car2['Ground_Clearance'])]
    kerb_weight_data = [float(car1['Kerb_Weight']), float(car2['Kerb_Weight'])]
    seating_capacity_data = [int(car1['Seating_Capacity']), int(car2['Seating_Capacity'])]
    boot_space_data = [float(car1['Boot_Space']), float(car2['Boot_Space'])]
    
    return render_template('results.html', 
                           make1=make1, model1=model1, variant1=variant1,
                           make2=make2, model2=model2, variant2=variant2,
                           ex_showroom_price_data=ex_showroom_price_data,
                           displacement_data=displacement_data,
                           fuel_type_data=fuel_type_data,
                           arai_certified_mileage_data=arai_certified_mileage_data,
                           fuel_tank_capacity_data=fuel_tank_capacity_data,
                           power_data=power_data,
                           torque_data=torque_data,
                           car_type_data=car_type_data,
                           cylinders_data=cylinders_data,
                           ground_clearance_data=ground_clearance_data,
                           kerb_weight_data=kerb_weight_data,
                           seating_capacity_data=seating_capacity_data,
                           boot_space_data=boot_space_data)

if __name__ == '__main__':
    app.run(debug=True)
