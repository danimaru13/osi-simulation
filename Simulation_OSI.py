# Simulation du modèle OSI

# ENCAPSULATION (ENVOI)

def application_layer(data):
    print("[Application] Données :", data)
    return data

def presentation_layer(data):
    data = f"<enc>{data}</enc>"
    print("[Présentation] Encodage :", data)
    return data

def session_layer(data):
    data = f"<session>{data}</session>"
    print("[Session] Session ouverte :", data)
    return data

def transport_layer(data):
    data = f"<tcp>{data}</tcp>"
    print("[Transport] Segment TCP :", data)
    return data

def network_layer(data):
    data = f"<ip>{data}</ip>"
    print("[Réseau] Adresse IP ajoutée :", data)
    return data

def datalink_layer(data):
    data = f"<mac>{data}</mac>"
    print("[Liaison] Adresse MAC ajoutée :", data)
    return data

def physical_layer(data):
    # Simulation binaire simple
    binary = ''.join(format(ord(c), '08b') for c in data)
    print("[Physique] Conversion en binaire :", binary)
    return binary


# DECAPSULATION (RECEPTION)

def physical_layer_decode(data):
    text = ''.join(chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8))
    print("[Physique] Binaire → Texte :", text)
    return text

def datalink_layer_decode(data):
    data = data.replace("<mac>", "").replace("</mac>", "")
    print("[Liaison] Suppression MAC :", data)
    return data

def network_layer_decode(data):
    data = data.replace("<ip>", "").replace("</ip>", "")
    print("[Réseau] Suppression IP :", data)
    return data

def transport_layer_decode(data):
    data = data.replace("<tcp>", "").replace("</tcp>", "")
    print("[Transport] Suppression TCP :", data)
    return data

def session_layer_decode(data):
    data = data.replace("<session>", "").replace("</session>", "")
    print("[Session] Fermeture session :", data)
    return data

def presentation_layer_decode(data):
    data = data.replace("<enc>", "").replace("</enc>", "")
    print("[Présentation] Décodage :", data)
    return data

def application_layer_decode(data):
    print("[Application] Message final :", data)
    return data


# FONCTIONS PRINCIPALES

def encapsulate(message):
    print("\n--- ENCAPSULATION ---\n")
    data = application_layer(message)
    data = presentation_layer(data)
    data = session_layer(data)
    data = transport_layer(data)
    data = network_layer(data)
    data = datalink_layer(data)
    data = physical_layer(data)
    return data


def decapsulate(data):
    print("\n--- DECAPSULATION ---\n")
    data = physical_layer_decode(data)
    data = datalink_layer_decode(data)
    data = network_layer_decode(data)
    data = transport_layer_decode(data)
    data = session_layer_decode(data)
    data = presentation_layer_decode(data)
    data = application_layer_decode(data)
    return data


# PROGRAMME PRINCIPAL

if __name__ == "__main__":
    message = input("Entrez un message : ")

    encoded = encapsulate(message)
    decoded = decapsulate(encoded)