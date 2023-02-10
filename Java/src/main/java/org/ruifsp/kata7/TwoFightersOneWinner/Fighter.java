package org.ruifsp.kata7.TwoFightersOneWinner;

public class Fighter {
    public String name;
    public int health, damagePerAttack;

    @Override
    public String toString() {
        return "Fighter{" +
                "name='" + name + '\'' +
                ", health=" + health +
                ", damagePerAttack=" + damagePerAttack +
                '}';
    }

    public Fighter(String name, int health, int damagePerAttack) {
        this.name = name;
        this.health = health;
        this.damagePerAttack = damagePerAttack;
    }
}
