# Returns True for prime n
def prime_check(n):
    if(n==2):
        return True
    elif((n<2) or ((n%2)==0)):
        return False
    elif(n>2):
        for i in range(2,n):
            if not(n%i):
                return False
    return True

# GCD FOR CALCULATING e
def egcd(e,r):
    while(r!=0):
        e, r = r, e%r
    return e

#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b == 0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return (gcd,t,s)
 
#Multiplicative Inverse, d such that 1 = (d*e) % r -> d is multiplicative inverse of e with respect to r
def mult_inv(e,r):
    gcd,t,s = eea(e,r)
    if(gcd != 1): # Guarenteed to be 1 in this code
        return None
    return t%r

#Encryption
def encrypt(pub_key,n_text):
    e,n=pub_key
    encrypted =[]
    m=0
    for i in n_text:
        m = ord(i)
        c = (m ** e) % n
        encrypted.append(c)
    return encrypted

#Decryption
def decrypt(priv_key,c_text):
    d,n = priv_key
    originalMSG = ''
    m=0
    for i in c_text:
        m = (i ** d) % n #ascII
        ch = chr(m) #itoa
        originalMSG += ch
    return originalMSG


if __name__ == '__main__':
    #Gather Prime Numbers
    while(1):
        p = int(input("Enter a prime number p: "))
        if (not prime_check(p)):
            print("*****************************************************")
            continue
        q = int(input("Enter a prime number q: "))
        if (not prime_check(q)):
            print("*****************************************************")
            continue
        print("*****************************************************")
        break
    
    #RSA Modulus n value
    n = p * q
    print("RSA Modulus n is: ",n)

    #Eulers Toitent
    r = (p - 1) * (q - 1)
    print("Eulers Toitent r is: ",r)
    print("*****************************************************")

    #e Value Calculation -- HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME
    for i in range(1,1000):
        if(egcd(i,r) == 1):
            e = i
    print("The value of e is:", e)
    print("*****************************************************")
    
    # CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY
    print("Multiplicative Inverse")
    d = mult_inv(e,r)
    print("The value of d is:",d)
    print("*****************************************************")

    public = (e,n)
    private = (d,n)
    print("Private Key:", private)
    print("Public Key:", public)
    print("*****************************************************")
    print("*****************************************************")

    while (1):
        #Choose Mode
        mode = int(input("Type int '1' for encryption or int '2' for decrytion or int 0 to QUIT: "))
        while ((mode != 0) and (mode != 1) and (mode != 2)):
            print("You entered the wrong option.")
            mode = int(input("Type '1' for encryption or '2' for decrytion or '0' to QUIT: "))

        if (mode == 0):
            print("cya")
            break
        elif (mode == 1):
            message = input("What would you like encrypted: ")
            enc_msg = encrypt(public,message)
            print("Your encrypted message is:",enc_msg)
            print("The decrypted message is:",decrypt(private, enc_msg))
            print("*****************************************************")
            print("*****************************************************")
        elif (mode == 2):
            message = input("What would you like to decrypted?(Separate numbers with ','): ")
            intlist = []
            intstrs = message.split(',')
            for i in intstrs:
                intlist.append(int(i))
            print("Your decrypted message is: ",decrypt(private, intlist))
            print("*****************************************************")
            print("*****************************************************")
        else:
            print(" ERROR\nShould Never Get Here!!")
            print("\n** ERR In RSA SIM **\n\n")