

f1 = open('20101539_Umme Abira Azmary_CSE422_11_Assignment02_Summer2024_InputFile.txt', 'r')
import random
PChromo = []
chromo = []

line1 = f1.readline().split()
N = int(line1[0])
T = int(line1[1])

hFitness = -100
hChromo = []

initial_flag = False

for i in range(10):
    for j in range(N*T):
      chromo.append(random.randint(0,1))
    PChromo.append(chromo)
    chromo = []
#print(PChromo)

for ksm in range(1000):
  #print(ksm)
  def crossover(c_lst):
    C_bonds = []
    crossChilds = []
    crossPoint = random.randint(3, 6)
    #print(crossPoint)

    for i in range(0, len(PChromo), 2):
      number1 = random.randint(0,8)
      C_bonds.append([PChromo[number1], PChromo[number1+1]])
    #print(C_bonds)

    for p in C_bonds:
      ch1 = p[0][:crossPoint]
      #print(ch1)
      back1 = p[0][crossPoint::]
      #print(back1)

      ch2 = p[1][:crossPoint]
      back2 = p[1][crossPoint::]
      #print(back2)

      child1 = ch1+back2
      crossChilds.append(child1)
      child2 = ch2+back1
      crossChilds.append(child2)

    #print(crossChilds)
    return crossChilds

  var = crossover(PChromo)

  def CMutate(c_lst):
    mutateChild = []
    for x in c_lst:

      indx = random.randint(2,6)
      val = random.randint(0, 1)

      c1 = x[0:indx]
      c2 = x[indx+1::]
      c1.append(val)
      mutate = c1+c2
      mutateChild.append(mutate)

    #print(c_lst)
    #print(mutateChild)
    return mutateChild

  mChild = CMutate(var)

  def fitness_test(f_lst):

    overlap_vals = []
    consistency_vals =[]
    overlapCourses = 0
    countOne = -1
    steps = 1

    for childs in f_lst:
      overlapCourses = 0
      for vals in childs:

        if int(vals) == 1:
          countOne += 1

        #print(steps)
        if steps % 3 == 0:
          if countOne >= 0:
            overlapCourses += countOne
          countOne = -1
        steps +=1
      overlap_vals.append(overlapCourses)
    # print(overlap_vals)

    consist = 0
    countONe = 0

    for p in f_lst:
      consist = 0
      for i in range(T):
        for q in range(0, len(p), T):
          #print(i+q)
          if p[i+q] == 1:
            countONe += 1


        if countONe > 1:
            consist += countONe -1
        elif countONe == 0:
            consist += 1
        countONe = 0
      consistency_vals.append(consist)
    #print(consistency_vals)

    fitness = [-u-v for u, v in zip(overlap_vals, consistency_vals)]
    return fitness

  fitness = fitness_test(mChild)


  temporarycount = 0

  for last in range(len(mChild)):
    if fitness[last] == 0:
      initial_flag = True
      hFitness = fitness[last]
      hChromo = mChild[last]
    elif fitness[last] > hFitness:
      hFitness = fitness[last]
      hChromo = mChild[last]
  if initial_flag:
    break

  # print(len(mChild))
  # print(len(fitness))
  PChromo = mChild




finalstring = ""

for word in hChromo:
  finalstring += str(word)
print(finalstring)
print(hFitness)