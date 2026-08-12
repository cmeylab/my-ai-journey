def embed(text:str,vec_dim:int=512)->list[float]:
    vec=[0.0]*vec_dim
    prime1=31
    prime2=131

    for ch in text:
        h=ord(ch)*prime1+prime2
        pos=h%vec_dim
        vec[pos]+=1

    for i in range(len(text)-1):
        c1,c2=text[i],text[i+1]
        h=ord(c1)*prime1*prime2+ord(c2)*prime1
        pos=h%vec_dim
        vec[pos]+=1.2

    norm = sum(x*x for x in vec)**0.5
    if norm >1e-8:
        vec=[x/norm for x in vec]
    return vec
def cos_sim(a:list[float],b:list[float])->float:
    return sum(x*y for x,y in zip(a,b))

