def addToInventory(inventory,addedItems):
    for item in addedItems:
        if item in  inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] =1
    return inventory



inv = {'goldcoin':42, 'rope': 1}
dragonLoot = ['goldcoin', 'dagger', 'goldcoin', 'goldcoin', 'ruby']
inv = addToInventory(inv,dragonLoot)

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k )
        item_total +=v
    print('Total number of items: ' + str(item_total))
displayInventory(inv)