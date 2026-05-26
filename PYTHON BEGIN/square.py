def square(number):
    return number * number
def main():
    
    number = int(input("Digite um número:\n"))
     
    quadrado = square(number)
    
    
    print(f"O quadrado de {number} é ", quadrado)
    
if __name__ == "__main__":
    main()