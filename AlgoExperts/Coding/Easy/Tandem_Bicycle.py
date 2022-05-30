def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    val = 0
    if fastest == True:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=True)
        for _ in range(len(redShirtSpeeds)):
            val += max(redShirtSpeeds[_], blueShirtSpeeds[_])
        return val
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        for _ in range(len(redShirtSpeeds)):
            val += max(redShirtSpeeds[_], blueShirtSpeeds[_])
        return val
    # return 0
