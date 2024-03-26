import voiceregoc as vc
from drawshapes import DrawShapes as DS

shape_dict = {0: 'circle', 3: 'triangle', 4: 'square', 4.5: 'rectangle', 5: 'pentagon', 6: 'hexagon', 7: 'septagon', 8: 'octagon', 9: 'nonagon', 10: 'decagon'}


while True:
    print('Painter: What do you want to draw?')
    vc.speak('What do you want to draw')
    voice_text = vc.interpretation()
    try:
        voice_text = voice_text.casefold()
    except:
        print('Painter: Please repeat again.')
        vc.speak('Please repeat again.')
        continue

    if voice_text == None or voice_text == "NoneType":
        print('Painter: Please repeat again.')
        vc.speak('Please repeat again.')
        continue

    if 'circle' in voice_text:
        nofsides = 0
    elif 'triangle' in voice_text:
        nofsides = 3
    elif 'rectangle' in voice_text:
        nofsides = 4.5
    elif 'square' in voice_text:
        nofsides = 4
    elif 'pentagon' in voice_text:
        nofsides = 5,
    elif 'hexagon' in voice_text:
        nofsides = 6
    elif 'septagon' in voice_text:
        nofsides = 7
    elif 'octagon' in voice_text:
        nofsides = 8
    elif 'nonagon' in voice_text:
        nofsides = 9
    elif 'decagon' in voice_text:
        nofsides = 10
    else:
        print('Painter: Please repeat again.')
        vc.speak('Please repeat again.')
        continue

    vc.speak('Drawing a ' + shape_dict[nofsides])
    p = DS(nofsides)
    p.setup()
    print('Painter: Would you like you draw again?')
    vc.speak('Would you like to draw again?')
    answer = vc.interpretation()

    try:
        answer = answer.casefold()
    except:
        print('Painter: Please repeat again.')
        vc.speak('Please repeat again.')
        continue
    
    if 'yes' in answer:
        p.clearScreen()
        continue
    elif 'no' in answer:
        break
    