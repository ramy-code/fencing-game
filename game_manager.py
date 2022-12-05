
class Scene:
    def __init__(self,scene_code):
        self.scene_code = scene_code
        self.char_1 = Character(1)
        self.char_2 = Character(2)
    def decode_scene(self,scene_code=None):
        if not scene_code:
            scene_code = self.scene_code
        self.length= 0
        self.obstacles_pos = []
        for char in scene_code:
            if char == '_':
                self.length += 2
            if char == '1' or char == '2' :
                character = getattr(self,f'char_{char}')
                setattr(character,'pos_x',self.length)
                self.length += self.char_1.width
            if char == 'x' :
                self.length += 1
                self.obstacles_pos.append(self.length)
        self.height = self.length // 2
    def draw_scene(self):
        canvas = [(" "*self.length) for i in range(self.height)]
        char_1_sprite,char_2_sprite = self.char_1.draw_character(),self.char_2.draw_character()
        ## pos players
        for p,char in zip([1,2],[char_1_sprite,char_2_sprite]):
            character = getattr(self,f'char_{p}')
            print(character.height)
            for i,j in zip(range(self.height-character.height-character.pos_y,self.height-character.pos_y),range(len(char))):
                canvas[i] = canvas[i][0:getattr(character,'pos_x')] + char[j] + canvas[i][getattr(character,'pos_x')+7:]
        ## pos obstacles
        for pos in self.obstacles_pos:
            for i in range(self.height-1,self.height):
                canvas[i] = canvas[i][0:pos] + "#" + canvas[i][pos+1:]
        canvas.append("_" * self.length)
        print("\n".join(canvas))
        self.canvas = canvas

class Character :
    def __init__(self,id,state = None , pos_x = None, pos_y = None,
                    stride = None, jump_height= None, movement_speed=None,
                        attack_range = None, attack_speed = None,
                        defending_range = None, block_duration = None):
        self.id = id
        self.state = 0 if not state else state
        self.pos_x = 0 if not pos_x else pos_x
        self.pos_y = 0 if not pos_y else pos_y
        self.is_jumping = False
        self.height = 4 
        self.width = 7
        self.stride = 1 if not stride else stride
        self.jump_height = 2 if not jump_height else jump_height
        self.movement_speed = 1 if not movement_speed else movement_speed
        self.attack_range = self.stride if not attack_range else attack_range
        self.attack_speed = self.movement_speed if not attack_speed else attack_speed
        self.defending_range = self.attack_range if not defending_range else defending_range
        self.block_duration = self.attack_speed if not block_duration else block_duration

    def draw_character(self):
        char_draw = []
        if self.state == 0:
            char_draw = self.draw_character_rest()
        if self.state == 1 :
            char_draw = self.draw_character_attack()
        if self.state == 2 :
            char_draw = self.draw_character_defense()
        return char_draw 


    def draw_character_rest(self):
        if self.id == 1 :
            return ["   O   ","  /|\\  ","   | \\ ","  / \  "]
        if self.id == 2 :
            return ["   O   ","  /|\\  "," / |   ","  / \  "]

    def draw_character_attack(self):
        if self.id == 1 :
            return ["   O   ","  /|\\_ ","   |   ","  / \  "]
        if self.id == 2 :
            return ["   O   "," _/|\\  ","   |   ","  / \  "]
    def draw_character_defense(self):
        if self.id == 1 :
            return ["   O   ","  /|\\| ","   |   ","  / \  "]
        if self.id == 2 :
            return ["   O   "," |/|\\  ","   |   ","  / \  "]