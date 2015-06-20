#s3overgang

**Abstract**

Een programma dat helpt bij de bepaling overgang van derde klassers

**notes voor development**

- beheren buttongroups

```python
# voeg eerst toe
self.$buttonName = QtGui.$QButtonType('$caption', self)
# maak group
self.$groupName = QtGui.QButtonGroup()
# voeg toe aan group, waar $id is int>0
self.$groupName.addButton(self.$buttonName, $id)
[...]
# controleer wat is gekozen
sig = self.$groupName.checkedId()
if sig == -1:
  print('niks gekozen')
elif sig == 1:
  print('$buttonID1 is gekozen')
elif sig == 2:
# enz
```

- behouden van variabelen

globale variabelen?


#### efkes op een rijtje

- 1 profiel
  - gemeenschappelijke vakken
  - 1 profielvak
  - 1 profielkeuzevak
    - let op: CM kiest 2
 - 1|2 extra vak
    - let op: geen conflict met PV of PKV

stel profielkeuzevakken CM `pr_gr_CM` dan

```python
# maak buttongroup, zie boven
# voeg knoppen toe aan buttongroup, zie boven
```
