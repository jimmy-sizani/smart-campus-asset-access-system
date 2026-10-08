#include <iostream>
#include <string>
using namespace std;

string classifyTemperature(double temperature) {
    if (temperature < 20.0) return "LOW";
    if (temperature <= 35.0) return "NORMAL";
    return "HIGH";
}

int main() {
    double temperature;
    cout << "Enter temperature in Celsius: ";
    cin >> temperature;
    cout << "Classification: " << classifyTemperature(temperature) << endl;
    return 0;
}
