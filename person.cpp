#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		float getDecades();
		long fib_mem();
		long fib();
	private:
		int age;
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

float Person::getDecades(){
	return (float)age/10;
	}

long Person::fib_mem(){
	int x = age;
	//Init memoization array (maximum age 999)
	long memory[1000] = {0};
	memory[0] = 0;
	memory[1] = 0;
	//Define lambda expression
	auto calc = [&memory, x](int n, auto& self) -> long{
		if(n <= 1){
			return n;
		}
		if(memory[n] == 0){
			memory[n] = (self(n-1, self) + self(n-2, self));
			return memory[n];
		}
		return memory[n];
	};
	//Execute lambda expression if age does not exceed 1000
	//Feeds the lambda expression along with the args to allow self-reference
	if(x > 999 || x < 0){
		return -1;
	}
	long y = calc(x, calc);
	return y;
} 

long Person::fib(){
	int x = age;
	//Define lambda expression
	auto calc = [x](int n, auto& self) -> long{
		if(n <= 1){
			return n;
		}
		return (self(n-1, self) + self(n-2, self));
	};
	//Execute lambda expression if age does not exceed 1000
	//Feeds the lambda expression along with the args to allow self-reference
	if(x > 999 || x < 0){
		return -1;
	}
	long y = calc(x, calc);
	return y;
}

extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	float Person_getDecades(Person* person) {return person->getDecades();}
	long Person_fib_mem(Person* person) {return person->fib_mem();}
	long Person_fib(Person* person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}