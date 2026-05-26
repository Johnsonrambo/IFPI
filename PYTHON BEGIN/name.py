def greet(nome):
    return nome

    
def main():
    
    nome = input("Digite seu nome :\n").strip()
    
    name = greet(nome)
    
    print(f"Hello,", nome)
    
if __name__ == "__main__":
    main()