# s3overgang

** Abstract **

Een programma die helpt bij de bepaling overgang 3deklassers

** notes voor development **

- beheren buttongroups

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

- behouden van variabelen

globale variabelen?
