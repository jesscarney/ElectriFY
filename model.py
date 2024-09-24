from pyomo.environ import *

model = AbstractModel()

##### sets, parameters, and variables

### time and location

model.time=Set()
model.location=Set()

model.time_steps=Param()
model.location_distance=Param(model.location,model.location)
model.invest_operate_ratio=Param()

### energy sources and uses

model.electric_source=Set()
model.fuel_source=Set()
model.heat_use=Set()
model.transport_use=Set()
model.fix_use=Set()

model.heat_demand=Param(model.heat_use,model.time,model.location)
model.transport_demand=Param(model.transport_use,model.time,model.location)
model.fix_demand_electric=Param(model.fix_use,model.time,model.location)
model.fix_demand_hydrogen=Param(model.fix_use,model.time,model.location)
model.fix_demand_fuel=Param(model.fuel_source,model.fix_use,model.time,model.location)

model.electric_supply=Var(model.time,model.location,within=NonNegativeReals)
model.hydrogen_supply=Var(model.time,model.location,within=NonNegativeReals)
model.fuel_supply=Var(model.fuel_source,model.time,model.location,within=NonNegativeReals)

### electric system

model.resource_availability=Param(model.electric_source,model.time,model.location)
model.generate_invest_cost=Param(model.electric_source)
model.generate_operate_cost=Param(model.electric_source)
model.generate_retire_cost=Param(model.electric_source)
model.generate_fuel_cost=Param(model.electric_source,model.time,model.location)
model.generate_efficiency=Param(model.electric_source)
model.generate_emit_rate=Param(model.electric_source)
model.store_invest_cost=Param()
model.store_operate_cost=Param()
model.store_retire_cost=Param()
model.store_efficiency=Param()
model.transmit_invest_cost=Param()
model.transmit_operate_cost=Param()
model.transmit_retire_cost=Param()
model.transmit_efficiency=Param()
model.generate_exist_capacity=Param(model.electric_source,model.location)
model.store_exist_capacity=Param(model.location)
model.transmit_exist_capacity=Param(model.location,model.location)

model.generate_new_capacity=Var(model.electric_source,model.location,within=NonNegativeReals)
model.generate_old_capacity=Var(model.electric_source,model.location,within=NonNegativeReals)
model.generate_energy=Var(model.electric_source,model.time,model.location,within=NonNegativeReals)
model.store_new_capacity=Var(model.location,within=NonNegativeReals)
model.store_old_capacity=Var(model.location,within=NonNegativeReals)
model.store_energy_input=Var(model.time,model.location,within=NonNegativeReals)
model.store_energy_level=Var(model.time,model.location,within=NonNegativeReals)
model.store_energy_output=Var(model.time,model.location,within=NonNegativeReals)
model.transmit_new_capacity=Var(model.location,model.location,within=NonNegativeReals)
model.transmit_old_capacity=Var(model.location,model.location,within=NonNegativeReals)
model.transmit_energy_transfer=Var(model.time,model.location,model.location,within=NonNegativeReals)

### hydrogen system

model.e2h_invest_cost=Param()
model.e2h_operate_cost=Param()
model.e2h_retire_cost=Param()
model.e2h_efficiency=Param()
model.h2e_invest_cost=Param()
model.h2e_operate_cost=Param()
model.h2e_retire_cost=Param()
model.h2e_efficiency=Param()
model.h2e_refit_cost=Param()
model.reserve_invest_cost=Param()
model.reserve_operate_cost=Param()
model.reserve_retire_cost=Param()
model.reserve_efficiency=Param()
model.reserve_refit_cost=Param()
model.reserve_max_flow=Param()
model.pipe_invest_cost=Param()
model.pipe_operate_cost=Param()
model.pipe_retire_cost=Param()
model.pipe_efficiency=Param()
model.pipe_refit_cost=Param()
model.e2h_exist_capacity=Param(model.location)
model.h2e_exist_capacity=Param(model.location)
model.reserve_exist_capacity=Param(model.location)
model.pipe_exist_capacity=Param(model.location,model.location)

model.e2h_new_capacity=Var(model.location,within=NonNegativeReals)
model.e2h_old_capacity=Var(model.location,within=NonNegativeReals)
model.e2h_energy_convert=Var(model.time,model.location,within=NonNegativeReals)
model.h2e_new_capacity=Var(model.location,within=NonNegativeReals)
model.h2e_old_capacity=Var(model.location,within=NonNegativeReals)
model.h2e_energy_convert=Var(model.time,model.location,within=NonNegativeReals)
model.reserve_new_capacity=Var(model.location,within=NonNegativeReals)
model.reserve_old_capacity=Var(model.location,within=NonNegativeReals)
model.reserve_energy_input=Var(model.time,model.location,within=NonNegativeReals)
model.reserve_energy_level=Var(model.time,model.location,within=NonNegativeReals)
model.reserve_energy_output=Var(model.time,model.location,within=NonNegativeReals)
model.pipe_new_capacity=Var(model.location,model.location,within=NonNegativeReals)
model.pipe_old_capacity=Var(model.location,model.location,within=NonNegativeReals)
model.pipe_energy_transfer=Var(model.time,model.location,model.location,within=NonNegativeReals)

### fuel system

model.fuel_cost=Param(model.fuel_source,model.time,model.location)
model.fuel_emit_rate=Param(model.fuel_source)
model.bioenergy_convert_efficiency=Param()

### supply/demand matching

model.match_invest_cost_electric_heat=Param(model.heat_use)
model.match_operate_cost_electric_heat=Param(model.heat_use)
model.match_retire_cost_electric_heat=Param(model.heat_use)
model.match_efficiency_electric_heat=Param(model.heat_use)
model.match_invest_cost_hydrogen_heat=Param(model.heat_use)
model.match_operate_cost_hydrogen_heat=Param(model.heat_use)
model.match_retire_cost_hydrogen_heat=Param(model.heat_use)
model.match_efficiency_hydrogen_heat=Param(model.heat_use)
model.match_invest_cost_fuel_heat=Param(model.fuel_source,model.heat_use)
model.match_operate_cost_fuel_heat=Param(model.fuel_source,model.heat_use)
model.match_retire_cost_fuel_heat=Param(model.fuel_source,model.heat_use)
model.match_efficiency_fuel_heat=Param(model.fuel_source,model.heat_use)
model.match_invest_cost_electric_transport=Param(model.transport_use)
model.match_operate_cost_electric_transport=Param(model.transport_use)
model.match_retire_cost_electric_transport=Param(model.transport_use)
model.match_efficiency_electric_transport=Param(model.transport_use)
model.match_invest_cost_hydrogen_transport=Param(model.transport_use)
model.match_operate_cost_hydrogen_transport=Param(model.transport_use)
model.match_retire_cost_hydrogen_transport=Param(model.transport_use)
model.match_efficiency_hydrogen_transport=Param(model.transport_use)
model.match_invest_cost_fuel_transport=Param(model.fuel_source,model.transport_use)
model.match_operate_cost_fuel_transport=Param(model.fuel_source,model.transport_use)
model.match_retire_cost_fuel_transport=Param(model.fuel_source,model.transport_use)
model.match_efficiency_fuel_transport=Param(model.fuel_source,model.transport_use)
model.match_exist_capacity_electric_heat=Param(model.heat_use,model.location)
model.match_exist_capacity_hydrogen_heat=Param(model.heat_use,model.location)
model.match_exist_capacity_fuel_heat=Param(model.fuel_source,model.heat_use,model.location)
model.match_exist_capacity_electric_transport=Param(model.transport_use,model.location)
model.match_exist_capacity_hydrogen_transport=Param(model.transport_use,model.location)
model.match_exist_capacity_fuel_transport=Param(model.fuel_source,model.transport_use,model.location)

model.match_new_capacity_electric_heat=Var(model.heat_use,model.location,within=NonNegativeReals)
model.match_old_capacity_electric_heat=Var(model.heat_use,model.location,within=NonNegativeReals)
model.match_new_capacity_hydrogen_heat=Var(model.heat_use,model.location,within=NonNegativeReals)
model.match_old_capacity_hydrogen_heat=Var(model.heat_use,model.location,within=NonNegativeReals)
model.match_new_capacity_fuel_heat=Var(model.fuel_source,model.heat_use,model.location,within=NonNegativeReals)
model.match_old_capacity_fuel_heat=Var(model.fuel_source,model.heat_use,model.location,within=NonNegativeReals)
model.match_new_capacity_electric_transport=Var(model.transport_use,model.location,within=NonNegativeReals)
model.match_old_capacity_electric_transport=Var(model.transport_use,model.location,within=NonNegativeReals)
model.match_new_capacity_hydrogen_transport=Var(model.transport_use,model.location,within=NonNegativeReals)
model.match_old_capacity_hydrogen_transport=Var(model.transport_use,model.location,within=NonNegativeReals)
model.match_new_capacity_fuel_transport=Var(model.fuel_source,model.transport_use,model.location,within=NonNegativeReals)
model.match_old_capacity_fuel_transport=Var(model.fuel_source,model.transport_use,model.location,within=NonNegativeReals)
model.match_energy_electric_heat=Var(model.heat_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_hydrogen_heat=Var(model.heat_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_fuel_heat=Var(model.fuel_source,model.heat_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_electric_transport=Var(model.transport_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_hydrogen_transport=Var(model.transport_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_fuel_transport=Var(model.fuel_source,model.transport_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_electric_fix=Var(model.fix_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_hydrogen_fix=Var(model.fix_use,model.time,model.location,within=NonNegativeReals)
model.match_energy_fuel_fix=Var(model.fuel_source,model.fix_use,model.time,model.location,within=NonNegativeReals)

### sustainability

model.hydro_limit=Param()
model.bioenergy_limit=Param()


### policy

model.emit_fix=Param()
model.emit_switch=Param()
model.emit_limit=Param(mutable=True)

model.emit_amount=Var(within=NonNegativeReals)

##### objective

def obj_rule(model):
	generate_cost=sum((model.generate_new_capacity[e,l]*model.generate_invest_cost[e]) for e in model.electric_source for l in model.location)+sum(((model.generate_new_capacity[e,l]+model.generate_exist_capacity[e,l])*model.generate_operate_cost[e]) for e in model.electric_source for l in model.location)-sum((model.generate_old_capacity[e,l]*model.generate_operate_cost[e]) for e in model.electric_source for l in model.location)+sum((model.generate_old_capacity[e,l]*model.generate_retire_cost[e]) for e in model.electric_source for l in model.location)+sum(((model.generate_energy[e,t,l]/model.generate_efficiency[e])*model.generate_fuel_cost[e,t,l]) for e in model.electric_source for t in model.time for l in model.location)*model.invest_operate_ratio
	store_cost=sum((model.store_new_capacity[l]*model.store_invest_cost) for l in model.location)+sum(((model.store_new_capacity[l]+model.store_exist_capacity[l])*model.store_operate_cost) for l in model.location)-sum((model.store_old_capacity[l]*model.store_operate_cost) for l in model.location)+sum((model.store_old_capacity[l]*model.store_retire_cost) for l in model.location)
	transmit_cost=sum((model.transmit_new_capacity[l,k]*model.transmit_invest_cost*model.location_distance[l,k]) for l in model.location for k in model.location)+sum(((model.transmit_new_capacity[l,k]+model.transmit_exist_capacity[l,k])*model.transmit_operate_cost*model.location_distance[l,k]) for l in model.location for k in model.location)-sum((model.transmit_old_capacity[l,k]*model.transmit_operate_cost*model.location_distance[l,k]) for l in model.location for k in model.location)+sum((model.transmit_old_capacity[l,k]*model.transmit_retire_cost*model.location_distance[l,k]) for l in model.location for k in model.location)
	e2h_cost=sum((model.e2h_new_capacity[l]*model.e2h_invest_cost) for l in model.location)+sum(((model.e2h_new_capacity[l]+model.e2h_exist_capacity[l])*model.e2h_operate_cost) for l in model.location)-sum((model.e2h_old_capacity[l]*model.e2h_operate_cost) for l in model.location)+sum((model.e2h_old_capacity[l]*model.e2h_retire_cost) for l in model.location)
	h2e_cost=sum((model.h2e_new_capacity[l]*model.h2e_invest_cost) for l in model.location)+sum((model.h2e_exist_capacity[l]*model.h2e_refit_cost) for l in model.location)+sum(((model.h2e_new_capacity[l]+model.h2e_exist_capacity[l])*model.h2e_operate_cost) for l in model.location)-sum((model.h2e_old_capacity[l]*model.h2e_operate_cost) for l in model.location)+sum((model.h2e_old_capacity[l]*model.h2e_retire_cost) for l in model.location)
	reserve_cost=sum((model.reserve_new_capacity[l]*model.reserve_invest_cost) for l in model.location)+sum((model.reserve_exist_capacity[l]*model.reserve_refit_cost) for l in model.location)+sum(((model.reserve_new_capacity[l]+model.reserve_exist_capacity[l])*model.reserve_operate_cost) for l in model.location)-sum((model.reserve_old_capacity[l]*model.reserve_operate_cost) for l in model.location)+sum((model.reserve_old_capacity[l]*model.reserve_retire_cost) for l in model.location)
	pipe_cost=sum((model.pipe_new_capacity[l,k]*model.pipe_invest_cost*model.location_distance[l,k]) for l in model.location for k in model.location)+sum((model.pipe_exist_capacity[l,k]*model.pipe_refit_cost*model.location_distance[l,k]) for l in model.location for k in model.location)+sum(((model.pipe_new_capacity[l,k]+model.pipe_exist_capacity[l,k])*model.pipe_operate_cost*model.location_distance[l,k]) for l in model.location for k in model.location)-sum((model.pipe_old_capacity[l,k]*model.pipe_operate_cost*model.location_distance[l,k]) for l in model.location for k in model.location)+sum((model.pipe_old_capacity[l,k]*model.pipe_retire_cost*model.location_distance[l,k]) for l in model.location for k in model.location)
	fuel_cost=sum((model.fuel_cost[f,t,l]*model.fuel_supply[f,t,l]) for f in model.fuel_source for t in model.time for l in model.location)*model.invest_operate_ratio
	match_cost_electric_heat=sum((model.match_new_capacity_electric_heat[u,l]*model.match_invest_cost_electric_heat[u]) for u in model.heat_use for l in model.location)+sum(((model.match_new_capacity_electric_heat[u,l]+model.match_exist_capacity_electric_heat[u,l])*model.match_operate_cost_electric_heat[u]) for u in model.heat_use for l in model.location)-sum((model.match_old_capacity_electric_heat[u,l]*model.match_operate_cost_electric_heat[u]) for u in model.heat_use for l in model.location)+sum((model.match_old_capacity_electric_heat[u,l]*model.match_retire_cost_electric_heat[u]) for u in model.heat_use for l in model.location)
	match_cost_hydrogen_heat=sum((model.match_new_capacity_hydrogen_heat[u,l]*model.match_invest_cost_hydrogen_heat[u]) for u in model.heat_use for l in model.location)+sum(((model.match_new_capacity_hydrogen_heat[u,l]+model.match_exist_capacity_hydrogen_heat[u,l])*model.match_operate_cost_hydrogen_heat[u]) for u in model.heat_use for l in model.location)-sum((model.match_old_capacity_hydrogen_heat[u,l]*model.match_operate_cost_hydrogen_heat[u]) for u in model.heat_use for l in model.location)+sum((model.match_old_capacity_hydrogen_heat[u,l]*model.match_retire_cost_hydrogen_heat[u]) for u in model.heat_use for l in model.location)
	match_cost_fuel_heat=sum((model.match_new_capacity_fuel_heat[f,u,l]*model.match_invest_cost_fuel_heat[f,u]) for f in model.fuel_source for u in model.heat_use for l in model.location)+sum(((model.match_new_capacity_fuel_heat[f,u,l]+model.match_exist_capacity_fuel_heat[f,u,l])*model.match_operate_cost_fuel_heat[f,u]) for f in model.fuel_source for u in model.heat_use for l in model.location)-sum((model.match_old_capacity_fuel_heat[f,u,l]*model.match_operate_cost_fuel_heat[f,u]) for f in model.fuel_source for u in model.heat_use for l in model.location)+sum((model.match_old_capacity_fuel_heat[f,u,l]*model.match_retire_cost_fuel_heat[f,u]) for f in model.fuel_source for u in model.heat_use for l in model.location)
	match_cost_electric_transport=sum((model.match_new_capacity_electric_transport[v,l]*model.match_invest_cost_electric_transport[v]) for v in model.transport_use for l in model.location)+sum(((model.match_new_capacity_electric_transport[v,l]+model.match_exist_capacity_electric_transport[v,l])*model.match_operate_cost_electric_transport[v]) for v in model.transport_use for l in model.location)-sum((model.match_old_capacity_electric_transport[v,l]*model.match_operate_cost_electric_transport[v]) for v in model.transport_use for l in model.location)+sum((model.match_old_capacity_electric_transport[v,l]*model.match_retire_cost_electric_transport[v]) for v in model.transport_use for l in model.location)
	match_cost_hydrogen_transport=sum((model.match_new_capacity_hydrogen_transport[v,l]*model.match_invest_cost_hydrogen_transport[v]) for v in model.transport_use for l in model.location)+sum(((model.match_new_capacity_hydrogen_transport[v,l]+model.match_exist_capacity_hydrogen_transport[v,l])*model.match_operate_cost_hydrogen_transport[v]) for v in model.transport_use for l in model.location)-sum((model.match_old_capacity_hydrogen_transport[v,l]*model.match_operate_cost_hydrogen_transport[v]) for v in model.transport_use for l in model.location)+sum((model.match_old_capacity_hydrogen_transport[v,l]*model.match_retire_cost_hydrogen_transport[v]) for v in model.transport_use for l in model.location)
	match_cost_fuel_transport=sum((model.match_new_capacity_fuel_transport[f,v,l]*model.match_invest_cost_fuel_transport[f,v]) for f in model.fuel_source for v in model.transport_use for l in model.location)+sum(((model.match_new_capacity_fuel_transport[f,v,l]+model.match_exist_capacity_fuel_transport[f,v,l])*model.match_operate_cost_fuel_transport[f,v]) for f in model.fuel_source for v in model.transport_use for l in model.location)-sum((model.match_old_capacity_fuel_transport[f,v,l]*model.match_operate_cost_fuel_transport[f,v]) for f in model.fuel_source for v in model.transport_use for l in model.location)+sum((model.match_old_capacity_fuel_transport[f,v,l]*model.match_retire_cost_fuel_transport[f,v]) for f in model.fuel_source for v in model.transport_use for l in model.location)
	return generate_cost+store_cost+transmit_cost+e2h_cost+h2e_cost+reserve_cost+pipe_cost+fuel_cost+match_cost_electric_heat+match_cost_hydrogen_heat+match_cost_fuel_heat+match_cost_electric_transport+match_cost_hydrogen_transport+match_cost_fuel_transport
model.obj=Objective(rule=obj_rule)

##### constraints

### electric/hydrogen energy flow

def electric_balance_rule(model,t,l):
        return sum(model.generate_energy[e,t,l] for e in model.electric_source)+(model.store_energy_output[t,l]*model.store_efficiency)+sum((model.transmit_energy_transfer[t,k,l]*model.transmit_efficiency) for k in model.location)+(model.h2e_energy_convert[t,l]*model.h2e_efficiency)==model.electric_supply[t,l]+model.store_energy_input[t,l]+sum(model.transmit_energy_transfer[t,l,k] for k in model.location)+model.e2h_energy_convert[t,l]
model.electric_balance=Constraint(model.time,model.location,rule=electric_balance_rule)

def hydrogen_balance_rule(model,t,l):
       return (model.e2h_energy_convert[t,l]*model.e2h_efficiency)+(model.reserve_energy_output[t,l]*model.reserve_efficiency)+sum((model.pipe_energy_transfer[t,k,l]*model.pipe_efficiency) for k in model.location)==model.hydrogen_supply[t,l]+model.reserve_energy_input[t,l]+sum(model.pipe_energy_transfer[t,l,k] for k in model.location)+model.h2e_energy_convert[t,l]
model.hydrogen_balance=Constraint(model.time,model.location,rule=hydrogen_balance_rule)

### supply/demand energy flow

def match_electric_supply_rule(model,t,l):
	return model.electric_supply[t,l]==sum(model.match_energy_electric_heat[u,t,l] for u in model.heat_use)+sum(model.match_energy_electric_transport[v,t,l] for v in model.transport_use)+sum(model.match_energy_electric_fix[w,t,l] for w in model.fix_use)
model.match_electric_supply=Constraint(model.time,model.location,rule=match_electric_supply_rule)

def match_hydrogen_supply_rule(model,t,l):
	return model.hydrogen_supply[t,l]==sum(model.match_energy_hydrogen_heat[u,t,l] for u in model.heat_use)+sum(model.match_energy_hydrogen_transport[v,t,l] for v in model.transport_use)+sum(model.match_energy_hydrogen_fix[w,t,l] for w in model.fix_use)
model.match_hydrogen_supply=Constraint(model.time,model.location,rule=match_hydrogen_supply_rule)

def match_fuel_supply_rule(model,f,t,l):
	return model.fuel_supply[f,t,l]==sum(model.match_energy_fuel_heat[f,u,t,l] for u in model.heat_use)+sum(model.match_energy_fuel_transport[f,v,t,l] for v in model.transport_use)+sum(model.match_energy_fuel_fix[f,w,t,l] for w in model.fix_use)
model.match_fuel_supply=Constraint(model.fuel_source,model.time,model.location,rule=match_fuel_supply_rule)

def match_heat_demand_rule(model,u,t,l):
	return model.heat_demand[u,t,l]==(model.match_energy_electric_heat[u,t,l]*model.match_efficiency_electric_heat[u])+(model.match_energy_hydrogen_heat[u,t,l]*model.match_efficiency_hydrogen_heat[u])+sum((model.match_energy_fuel_heat[f,u,t,l]*model.match_efficiency_fuel_heat[f,u]) for f in model.fuel_source)
model.match_heat_demand=Constraint(model.heat_use,model.time,model.location,rule=match_heat_demand_rule)

def match_transport_demand_rule(model,v,t,l):
	return model.transport_demand[v,t,l]==(model.match_energy_electric_transport[v,t,l]*model.match_efficiency_electric_transport[v])+(model.match_energy_hydrogen_transport[v,t,l]*model.match_efficiency_hydrogen_transport[v])+sum((model.match_energy_fuel_transport[f,v,t,l]*model.match_efficiency_fuel_transport[f,v]) for f in model.fuel_source)
model.match_transport_demand=Constraint(model.transport_use,model.time,model.location,rule=match_transport_demand_rule)

def match_fix_electric_demand_rule(model,w,t,l):
	return model.fix_demand_electric[w,t,l]==model.match_energy_electric_fix[w,t,l]
model.match_fix_electric_demand=Constraint(model.fix_use,model.time,model.location,rule=match_fix_electric_demand_rule)

def match_fix_hydrogen_demand_rule(model,w,t,l):
	return model.fix_demand_hydrogen[w,t,l]==model.match_energy_hydrogen_fix[w,t,l]
model.match_fix_hydrogen_demand=Constraint(model.fix_use,model.time,model.location,rule=match_fix_hydrogen_demand_rule)

def match_fix_fuel_demand_rule(model,f,w,t,l):
	return model.fix_demand_fuel[f,w,t,l]==model.match_energy_fuel_fix[f,w,t,l]
model.match_fix_fuel_demand=Constraint(model.fuel_source,model.fix_use,model.time,model.location,rule=match_fix_fuel_demand_rule)

### electric equipment capacity

def max_generate_rule(model,e,t,l):
        return model.generate_energy[e,t,l]<=((model.generate_new_capacity[e,l]+model.generate_exist_capacity[e,l]-model.generate_old_capacity[e,l])*model.resource_availability[e,t,l])
model.max_generate=Constraint(model.electric_source,model.time,model.location,rule=max_generate_rule)

def max_store_rule(model,t,l):
        return model.store_energy_level[t,l]<=(model.store_new_capacity[l]+model.store_exist_capacity[l]-model.store_old_capacity[l])
model.max_store=Constraint(model.time,model.location,rule=max_store_rule)

def store_continuity_rule(model,t,l):
        if t==1:
                return model.store_energy_level[t,l]==(model.store_energy_level[model.time_steps,l]+model.store_energy_input[t,l]-model.store_energy_output[t,l])
        else:
                return model.store_energy_level[t,l]==(model.store_energy_level[t-1,l]+model.store_energy_input[t,l]-model.store_energy_output[t,l])
model.store_continuity=Constraint(model.time,model.location,rule=store_continuity_rule)

def first_last_store_rule(model,l):
        return model.store_energy_level[1,l]==model.store_energy_level[model.time_steps,l]
model.first_last_store=Constraint(model.location,rule=first_last_store_rule)

def max_transmit_rule(model,t,l,k):
        return model.transmit_energy_transfer[t,l,k]<=(model.transmit_new_capacity[l,k]+model.transmit_exist_capacity[l,k]-model.transmit_old_capacity[l,k])
model.max_transmit=Constraint(model.time,model.location,model.location,rule=max_transmit_rule)

def bidirectional_transmit_rule(model,l,k):
        return (model.transmit_new_capacity[l,k]+model.transmit_exist_capacity[l,k]-model.transmit_old_capacity[l,k])==(model.transmit_new_capacity[k,l]+model.transmit_exist_capacity[k,l]-model.transmit_old_capacity[k,l])
model.bidirectional_transmit=Constraint(model.location,model.location,rule=bidirectional_transmit_rule)

def different_location_transmit_rule(model,l):
	return (model.transmit_new_capacity[l,l]+model.transmit_exist_capacity[l,l]-model.transmit_old_capacity[l,l])==0
model.different_location_transmit=Constraint(model.location,rule=different_location_transmit_rule)

### hydrogen equipment capacity

def max_e2h_rule(model,t,l):
        return model.e2h_energy_convert[t,l]*model.e2h_efficiency<=(model.e2h_new_capacity[l]+model.e2h_exist_capacity[l]-model.e2h_old_capacity[l])
model.max_e2h=Constraint(model.time,model.location,rule=max_e2h_rule)

def max_h2e_rule(model,t,l):
        return model.h2e_energy_convert[t,l]*model.h2e_efficiency<=(model.h2e_new_capacity[l]+model.h2e_exist_capacity[l]-model.h2e_old_capacity[l])
model.max_h2e=Constraint(model.time,model.location,rule=max_h2e_rule)

def max_reserve_rule(model,t,l):
        return model.reserve_energy_level[t,l]<=(model.reserve_new_capacity[l]+model.reserve_exist_capacity[l]-model.reserve_old_capacity[l])
model.max_reserve=Constraint(model.time,model.location,rule=max_reserve_rule)

def max_reserve_input_rule(model,t,l):
	return model.reserve_energy_input[t,l]<=(model.reserve_new_capacity[l]+model.reserve_exist_capacity[l]-model.reserve_old_capacity[l])*model.reserve_max_flow
model.max_reserve_input=Constraint(model.time,model.location,rule=max_reserve_input_rule)

def max_reserve_output_rule(model,t,l):
	return model.reserve_energy_output[t,l]<=(model.reserve_new_capacity[l]+model.reserve_exist_capacity[l]-model.reserve_old_capacity[l])*model.reserve_max_flow
model.max_reserve_output=Constraint(model.time,model.location,rule=max_reserve_output_rule)

def reserve_continuity_rule(model,t,l):
        if t==1:
                return model.reserve_energy_level[t,l]==(model.reserve_energy_level[model.time_steps,l]+model.reserve_energy_input[t,l]-model.reserve_energy_output[t,l])
        else:
                return model.reserve_energy_level[t,l]==(model.reserve_energy_level[t-1,l]+model.reserve_energy_input[t,l]-model.reserve_energy_output[t,l])
model.reserve_continuity=Constraint(model.time,model.location,rule=reserve_continuity_rule)

def first_last_reserve_rule(model,l):
        return model.reserve_energy_level[1,l]==model.reserve_energy_level[model.time_steps,l]
model.first_last_reserve=Constraint(model.location,rule=first_last_reserve_rule)

def max_pipe_rule(model,t,l,k):
        return model.pipe_energy_transfer[t,l,k]<=(model.pipe_new_capacity[l,k]+model.pipe_exist_capacity[l,k]-model.pipe_old_capacity[l,k])
model.max_pipe=Constraint(model.time,model.location,model.location,rule=max_pipe_rule)

def bidirectional_pipe_rule(model,l,k):
        return (model.pipe_new_capacity[l,k]+model.pipe_exist_capacity[l,k]-model.pipe_old_capacity[l,k])==(model.pipe_new_capacity[k,l]+model.pipe_exist_capacity[k,l]-model.pipe_old_capacity[k,l])
model.bidirectional_pipe=Constraint(model.location,model.location,rule=bidirectional_pipe_rule)

def different_location_pipe_rule(model,l):
	return (model.pipe_new_capacity[l,l]+model.pipe_exist_capacity[l,l]-model.pipe_old_capacity[l,l])==0
model.different_location_pipe=Constraint(model.location,rule=different_location_pipe_rule)

### matching equipment capacity

def max_match_electric_heat_rule(model,u,t,l):
	return (model.match_energy_electric_heat[u,t,l]*model.match_efficiency_electric_heat[u])<=(model.match_new_capacity_electric_heat[u,l]+model.match_exist_capacity_electric_heat[u,l]-model.match_old_capacity_electric_heat[u,l])
model.max_match_electric_heat=Constraint(model.heat_use,model.time,model.location,rule=max_match_electric_heat_rule)

def max_match_hydrogen_heat_rule(model,u,t,l):
	return (model.match_energy_hydrogen_heat[u,t,l]*model.match_efficiency_hydrogen_heat[u])<=(model.match_new_capacity_hydrogen_heat[u,l]+model.match_exist_capacity_hydrogen_heat[u,l]-model.match_old_capacity_hydrogen_heat[u,l])
model.max_match_hydrogen_heat=Constraint(model.heat_use,model.time,model.location,rule=max_match_hydrogen_heat_rule)

def max_match_fuel_heat_rule(model,f,u,t,l):
	return (model.match_energy_fuel_heat[f,u,t,l]*model.match_efficiency_fuel_heat[f,u])<=(model.match_new_capacity_fuel_heat[f,u,l]+model.match_exist_capacity_fuel_heat[f,u,l]-model.match_old_capacity_fuel_heat[f,u,l])
model.max_match_fuel_heat=Constraint(model.fuel_source,model.heat_use,model.time,model.location,rule=max_match_fuel_heat_rule)

def max_match_electric_transport_rule(model,v,t,l):
	return (model.match_energy_electric_transport[v,t,l]*model.match_efficiency_electric_transport[v])<=(model.match_new_capacity_electric_transport[v,l]+model.match_exist_capacity_electric_transport[v,l]-model.match_old_capacity_electric_transport[v,l])
model.max_match_electric_transport=Constraint(model.transport_use,model.time,model.location,rule=max_match_electric_transport_rule)

def max_match_hydrogen_transport_rule(model,v,t,l):
	return (model.match_energy_hydrogen_transport[v,t,l]*model.match_efficiency_hydrogen_transport[v])<=(model.match_new_capacity_hydrogen_transport[v,l]+model.match_exist_capacity_hydrogen_transport[v,l]-model.match_old_capacity_hydrogen_transport[v,l])
model.max_match_hydrogen_transport=Constraint(model.transport_use,model.time,model.location,rule=max_match_hydrogen_transport_rule)

def max_match_fuel_transport_rule(model,f,v,t,l):
	return (model.match_energy_fuel_transport[f,v,t,l]*model.match_efficiency_fuel_transport[f,v])<=(model.match_new_capacity_fuel_transport[f,v,l]+model.match_exist_capacity_fuel_transport[f,v,l]-model.match_old_capacity_fuel_transport[f,v,l])
model.max_match_fuel_transport=Constraint(model.fuel_source,model.transport_use,model.time,model.location,rule=max_match_fuel_transport_rule)

### sustainability

def hydro_limit_enforce_rule(model):
	return sum(model.generate_energy['hydro',t,l] for t in model.time for l in model.location)*model.invest_operate_ratio<=model.hydro_limit
model.hydro_limit_enforce=Constraint(rule=hydro_limit_enforce_rule)

def bioenergy_limit_enforce_rule(model):
        return (sum(model.fuel_supply['biomass',t,l] for t in model.time for l in model.location)+sum((model.fuel_supply['biofuel',t,l]/model.bioenergy_convert_efficiency) for t in model.time for l in model.location)+sum((model.generate_energy['bioenergy',t,l]/model.generate_efficiency['bioenergy']) for t in model.time for l in model.location))*model.invest_operate_ratio<=model.bioenergy_limit
model.bioenergy_limit_enforce=Constraint(rule=bioenergy_limit_enforce_rule)

### policy 

def emit_amount_calculate_rule(model):
        return model.emit_amount==(sum((model.fuel_supply[f,t,l]*model.fuel_emit_rate[f]) for f in model.fuel_source for t in model.time for l in model.location)+sum(((model.generate_energy[e,t,l]/model.generate_efficiency[e])*model.generate_emit_rate[e]) for e in model.electric_source for t in model.time for l in model.location))*model.invest_operate_ratio
model.emit_amonut_calculate=Constraint(rule=emit_amount_calculate_rule)

def emit_limit_enforce_rule(model):
        return model.emit_amount<=model.emit_fix+(model.emit_limit*model.emit_switch)
model.emit_limit_enforce=Constraint(rule=emit_limit_enforce_rule)