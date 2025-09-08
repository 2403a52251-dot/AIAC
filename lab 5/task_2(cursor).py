import json
from datetime import datetime

class LoanBiasTester:
    """AI Bias Testing Framework - 50 lines"""
    
    def __init__(self):
        self.results = []
        self.names = {
            'male': ['John', 'Michael', 'David', 'James', 'Robert'],
            'female': ['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth'],
            'diverse': ['Priya', 'Aisha', 'Chen', 'Hassan', 'Maria']
        }
        self.scenario = {'income': 50000, 'credit_score': 720, 'debt_to_income': 0.25, 'employment_years': 3}
    
    def simulate_decision(self, app):
        """Simulate AI loan decision with bias"""
        score = 0
        if app['credit_score'] >= 700: score += 30
        if app['income'] >= 50000: score += 20
        if app['debt_to_income'] <= 0.30: score += 15
        if app['employment_years'] >= 3: score += 10
        
        # BIAS INJECTION
        bias = 0
        if app['gender'] == 'female': bias -= 5
        elif app['gender'] == 'diverse': bias -= 8
        if app['name'] in ['Priya', 'Aisha', 'Chen', 'Hassan']: bias -= 3
        
        final_score = score + bias
        return {'approved': final_score >= 60, 'score': final_score, 'bias': bias}
    
    def run_tests(self):
        """Run bias tests with prompt variations"""
        print("🔍 AI Bias Testing: Loan Approval System")
        print("=" * 45)
        
        for gender, names in self.names.items():
            for name in names:
                app = self.scenario.copy()
                app.update({'name': name, 'gender': gender, 'prompt': f"loan approval for {name}"})
                
                decision = self.simulate_decision(app)
                result = {
                    'name': name, 'gender': gender, 'prompt': app['prompt'],
                    'approved': decision['approved'], 'score': decision['score'], 'bias': decision['bias']
                }
                self.results.append(result)
        
        self.analyze()
    
    def analyze(self):
        """Analyze bias patterns"""
        print("\n📊 Results by Gender:")
        for gender in ['male', 'female', 'diverse']:
            gender_results = [r for r in self.results if r['gender'] == gender]
            approval_rate = sum(r['approved'] for r in gender_results) / len(gender_results) * 100
            avg_bias = sum(r['bias'] for r in gender_results) / len(gender_results)
            print(f"   {gender.upper()}: {approval_rate:.0f}% approved, {avg_bias:.1f} avg bias")
        
        # Detect bias
        rates = []
        for gender in ['male', 'female', 'diverse']:
            gender_results = [r for r in self.results if r['gender'] == gender]
            rate = sum(r['approved'] for r in gender_results) / len(gender_results) * 100
            rates.append(rate)
        
        max_diff = max(rates) - min(rates)
        bias_level = "🚨 HIGH" if max_diff > 15 else "⚠️ MODERATE" if max_diff > 8 else "✅ LOW"
        print(f"\n⚠️ BIAS DETECTION: {bias_level} ({max_diff:.0f}% difference)")
        
        # Save results
        with open(f"bias_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n💾 Results saved to JSON file")

def main():
    tester = LoanBiasTester()
    print("🤖 AI Bias Testing Framework")
    print("Testing prompt variations like 'loan approval for John', 'loan approval for Priya'")
    print()
    tester.run_tests()

if __name__ == "__main__":
    main()