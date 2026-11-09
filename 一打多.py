import os
import time
import random
from email.mime import base

from types import TracebackType



class Ninja:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.energy =0
        self.potions = 3
        self.is_edo = False
        self.is_kurama = False
    def attack(self, enemy):

        self.energy = self.energy +40
        print(f"{self.name}发动飞雷神！(积攒40点能量，当前能量:{self.energy}")
        print(f"⚡【{self.name}】发动飞雷神，闪到【{enemy.name}】背后！")
        dodge_dice = random.randint(1, 10)
        if dodge_dice >= 9:
            print("给怪物躲了过去，可惜")
        else:
            real_dmg = random.randint(self.atk - 20, self.atk + 100)
            crit_dice = random.randint(1, 10)
            if crit_dice >= 8:
             real_dmg = real_dmg * 2
             print(f"✨【被动触发】飞雷神二段！时空忍术的无情连打！")
             enemy.hp = enemy.hp - real_dmg
            print(f"【{enemy.name}】受到了 {real_dmg} 点伤害！剩余血量: {enemy.hp}")
    def heal(self):
        self.potions = (self.potions - 1)
        self.hp = self.hp + 300
        print(f"【{self.name}】使用了秘药，恢复了 300 点血量！当前血量: {self.hp}")
    def rasengan(self,enemy):
        self.atk = (self.atk + 50)

        print(f"【{self.name}】手中凝聚出高密度查克拉，大喊：螺旋丸！！")
        if self.is_edo == False:
            self.energy = self.energy - 100
        else:
            print("🌀【无限查克拉】秽土转生状态下，大招不消耗任何能量！")
        dodge_dice = random.randint(1, 10)
        if dodge_dice >= 8:
            print("怪物向后跳了一步 躲过了这招")
        else:
            real_dmg = random.randint(self.atk - 20, self.atk + 100)
            enemy.hp = enemy.hp - real_dmg
            print(f"【{enemy.name}】被螺旋丸正中，受到了 {real_dmg} 点巨额伤害！剩余血量: {enemy.hp}")
    def edo_tensei(self):
        self.is_edo = True
        self.name = "波风水门【秽土转生】"
        self.hp = self.max_hp +9999
        self.atk = self.atk + 800
        self.energy = 100
        print(f"\n 【禁术发动】纸屑飞舞，水门的身体重组了！")
        print(f" 【{self.name}】降临擂台！血量暴涨至 {self.hp}，攻击飙升，查克拉拉满！")
    def kurama_mode(self):
        self.is_kurama = True
        self.name = "波风水门【九喇嘛连结】"
        self.hp = self.max_hp +99999
        self.atk = self.atk + 1500
        self.energy = 200
        print(f"\n 九尾查克拉爆发】金色的查克拉外衣披挂在身！")
        print(f" 【{self.name}】参战！攻击力突破天际！")

class Monster:
    def __init__(self, name, hp, atk,skill_name):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.energy = 0
        self.potions = 2
        self.skill_name = skill_name
    def attack(self, enemy):


        print(f"【{self.name}】愤怒咆哮，挥舞大棒砸向【{enemy.name}】！")
        dodge_dice = random.randint(1, 10)
        if dodge_dice >= 9:
            print(f"💨 唰！金色闪光！【{enemy.name}】看穿了动作，完美闪避了这次攻击！")
        else:
          real_dmg = random.randint(self.atk - 1000, self.atk + 3000)
          enemy.hp = enemy.hp - real_dmg
          print(f"【{enemy.name}】受到了 {real_dmg} 点伤害！剩余血量: {enemy.hp}")
    def heal(self):
        self.potions = (self.potions - 1)
        self.hp = self.hp + 200
        print("怪物使用了药水 回复了200点血")
    def renya(self,enemy):
        self.atk = (self.atk + 70)

        print(f"{self.name}面露凶光，使出了绝招{self.skill_name}！")
        dodge_dice = random.randint(1, 10)
        if dodge_dice >= 10:
         print(f" 唰！【{enemy.name}】发动飞雷神瞬间转移，惊险躲过了致命一击！")
        else:
         real_dmg = random.randint(self.atk - 20, self.atk + 100)
         enemy.hp = enemy.hp - real_dmg
         print(f"【{enemy.name}】被重创，受到了 {real_dmg} 点巨额伤害！")


minato = Ninja("波风水门", 900, 200)

boss_list = [
    Monster("哥布林小兵", 300, 50,"狼牙棒闷棍"),
    Monster("哥布林大祭司", 600, 80,"暗影邪毒诅咒"),
    Monster("深渊魔王", 1200, 120,"灭世地狱业火")
]


print("=== ⚔️ 水门的地狱闯关模式开始！ ⚔️ ===")
time.sleep(1)


for target in boss_list:
    print(f"\n🔥🔥 红色警报：【{target.name}】登场了！🔥🔥")
    time.sleep(1)


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n====================")

        print(f"❤ 水门 HP: {minato.hp}  |   能量: {minato.energy}/100")
        print("请选择水门的动作：")
        print("1. 飞雷神 (攒 40 能量)")
        print("2. 螺旋丸 (耗 100 能量)")
        print("3. 喝秘药")
        print("4. 觉醒九喇嘛 (条件: 秽土状态 + HP低于5000)")
        print("====================")

        choice = input("请输入指令编号 (1/2/3/4): ")
        if choice == "1":
            minato.attack(target)
        elif choice == "2":
            if minato.energy >= 100:
                minato.rasengan(target)
            else:
             print("能量不足 100！无法释放大招！请重新选择！")
             continue
        elif choice == "3":
            if minato.potions > 0:
                minato.heal()
            else:
                print("没有药了 使用失败")


        elif choice == "4":
            if minato.is_edo == True and minato.hp < 5000 and minato.is_kurama == False:
                minato.kurama_mode()
            else:
                print("⚠️ 觉醒失败！条件未满足（必须在秽土状态、血量低于5000、且未开启过）！请重新选择！")
                continue


        else:
            print("没有这个选项 重新选吧")
            continue


        if target.hp <= 0:
            print(f"🎉 华丽击杀！水门战胜了 {target.name}！准备迎接下一个！")
            drop_dice = random.randint(1, 2)
            minato.potions = minato.potions + drop_dice
            print(f" 水门从 {target.name} 身上搜刮出了 {drop_dice} 瓶秘药！当前秘药: {minato.potions} 瓶")
            break

        time.sleep(0.5)

        # 3. 怪物反击 (这里的缩进也要和上面的 if target.hp <= 0 平齐)
        monster_dice = random.randint(1, 10)
        if monster_dice >= 8:
            target.renya(minato)
        else:
            target.attack(minato)


        if minato.hp <= 0:
            if minato.is_edo == False:
                minato.edo_tensei()
            else:
                print(f" 彻底耗尽 {minato.name} 被 {target.name} 击败，闯关失败！")
                break

        time.sleep(1)


    if minato.hp <= 0:
        print("\n游戏结束，胜败乃兵家常事。")
        break


if minato.hp > 0:
    print("\n 【终极通关】太强了！波风水门全歼了怪物大军，赢得了最终的胜利！")