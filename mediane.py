def mediane(notes):
    tri=sorted(notes)
    n=len(tri)
    return tri[n//2]
notes=[4,8,12,19,39]
print("mediane:",mediane(notes))