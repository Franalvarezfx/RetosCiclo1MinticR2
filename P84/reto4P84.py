def conversion(datos:tuple)->list:
    lista1 = list(filter(lambda y: y>=40,map(lambda x: round((1.1*x*100)/1024,1),datos)))
    lista2 = list(filter(lambda y: y<40,map(lambda x: round((1.1*x*100)/1024,1),datos)))
    Lista_salida=[lista1,len(lista1),lista2,len(lista2)]
  
    return Lista_salida

datos = (224, 216, 296, 204, 324, 360, 379, 335, 299, 328, 267, 248, 399, 393, 280, 211, 341, 433, 238, 206, 301, 209, 309, 391, 220, 296, 402, 347, 312, 321, 252, 347, 269, 318, 205, 211, 261, 345, 395, 309, 347, 222, 351, 272, 222, 356, 386, 259, 428, 304, 205, 314, 371, 416, 249, 322, 333, 328, 430, 393, 347, 232, 349, 275, 405, 243, 271, 342, 415, 422, 205, 291)
print(conversion(datos))

datos = (435, 338, 312, 410, 405, 240, 273, 381, 337, 316, 386, 366, 430, 317, 228, 425, 383, 418, 316, 375, 432, 388, 319, 415, 245, 430, 373, 360, 281, 360, 357, 290, 400, 376, 212, 238, 239, 400, 376, 420, 367, 276, 229, 274, 207, 259, 353, 316, 307, 239, 225, 415, 385, 366, 376, 394, 353, 328, 392, 299, 233, 432, 218, 404, 365, 295, 325, 213, 364, 263, 362, 365)
print(conversion(datos))

datos = (257, 201, 277, 417, 235, 367, 247, 200, 410, 262, 282, 232, 396, 202, 232, 418, 362, 420, 349, 256, 347, 235, 332, 246, 203, 334, 221, 403, 409, 329, 224, 357, 348, 221, 374, 263, 325, 218, 440, 434, 372, 324, 345, 272, 430, 234, 404, 321, 294, 421, 318, 308, 349, 318, 374, 393, 254, 398, 219, 280, 411, 332, 301, 323, 430, 354, 238, 232, 301, 266, 297, 317)
print(conversion(datos))

datos = (268, 410, 353, 252, 227, 263, 362, 411, 369, 391, 207, 354, 311, 340, 260, 338, 257, 331, 438, 396, 303, 378, 418, 337, 381, 324, 228, 309, 312, 301, 325, 324, 286, 317, 417, 372, 230, 300, 329, 340, 430, 286, 342, 401, 320, 245, 263, 342, 265, 309, 355, 259, 291, 249, 250, 299, 323, 287, 388, 352, 413, 322, 427, 347, 291, 284, 281, 419, 261, 350, 207, 251)
print(conversion(datos))