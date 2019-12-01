# -*- coding: UTF-8 -*-

from gurobipy import *


interviews=tuplelist([
('Alex','Company 1','10:00'),
('Alex','Company 1','11:00'),
('Alex','Company 1','13:00'),
('Bob','Company 1','09:00'),
('Bob','Company 1','10:00'),
('Bob','Company 1','11:00'),
('Caroline','Company 1','09:00'),
('Caroline','Company 1','10:00'),
('Caroline','Company 1','11:00'),
('Doris','Company 1','09:00'),
('Doris','Company 1','10:00'),
('Doris','Company 1','11:00'),
('Alex','Company 2','10:00'),
('Alex','Company 2','11:00'),
('Alex','Company 2','13:00'),
('Caroline','Company 2','09:00'),
('Caroline','Company 2','10:00'),
('Caroline','Company 2','11:00'),
('Fredrik','Company 2','09:00'),
('Fredrik','Company 2','10:00'),
('Fredrik','Company 2','11:00'),
('Alex','Company 3','10:00'),
('Alex','Company 3','11:00'),
('Alex','Company 3','13:00'),
('Bob','Company 3','10:00'),
('Bob','Company 3','11:00'),
('Bob','Company 3','13:00'),
('Edward','Company 3','10:00'),
('Edward','Company 3','11:00'),
('Edward','Company 3','13:00'),
])
#
# interviews = tuplelist([
# ('Amy','companyA',1),('Amy','companyA',2),
# ('Amy','companyB',3),('Amy','companyB',2),
# ('Amy','companyA',4),('Amy','companyA',5),
# ('Amy','companyA',6),('Amy','companyA',3),
# ('Bobby','companyA',1),('Bobby','companyA',2),
# ('Bobby','companyB',1),('Bobby','companyB',2),
# ('Carro','companyA',4),('Carro','companyB',2)
# ])
# interviews = tuplelist([
# ('Amy','companyA',1),('Bob','companyA',2),('Cat','companyA',3),
# ('Amy','companyB',1),('Bob','companyA',1)
# ])

# Model
m = Model("schema")

x = m.addVars(interviews, ub=1, name="x", vtype=GRB.INTEGER)

# The objective is to maximize number of students that get interviews
m.setObjective(quicksum(x[s,f,t] for s,f,t in interviews), GRB.MAXIMIZE)

# that a company can only have one interview per time slot.
m.addConstrs((x.sum('*',f,t)<=1
                        for s,f,t in interviews))

# that a student can only go to one interview for every time slot.
m.addConstrs((x.sum(s,'*',t)<=1
                        for s,f,t in interviews))

# that a student _will_ go to an interview one time.
m.addConstrs((x.sum(s,f,'*')==1
                        for s,f,t in interviews))

# Save model
m.write('ks.lp')
# Optimize
m.optimize()
status = m.status
f = open("schedule.csv","w+")
if status == GRB.Status.UNBOUNDED:
    print('The model cannot be solved because it is unbounded')
    exit(0)
if status == GRB.Status.OPTIMAL:
    print('The optimal objective is %g' % m.objVal)
    for v in m.getVars():
        if v.x !=0:
            #print(v.x)
            # removes the first x[ and the last ] for csv format
            f.write(v.varname[2:-1]+"\n")

    f.close()
    exit(0)
if status != GRB.Status.INF_OR_UNBD and status != GRB.Status.INFEASIBLE:
    print('Optimization was stopped with status %d' % status)
    exit(0)

# do IIS
print('The model is infeasible; computing IIS')
m.computeIIS()
if m.IISMinimal:
  print('IIS is minimal\n')
else:
  print('IIS is not minimal\n')
print('\nThe following constraint(s) cannot be satisfied:')
for c in m.getConstrs():
    if c.IISConstr:
        print('%s' % c.constrName)
