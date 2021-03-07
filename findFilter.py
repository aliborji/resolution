import numpy as np



# def find_res_fixed_params(N, C1, K1, B1, K3, P1, S1, Q1, R1):
#   '''
#     Keeping the number of parameters the same
#     Approach III in the paper
#   '''
#   # N1=20 # orig image size

#   # # layer 1
#   # C1=3 # filter size old
#   # K1=20  # num filters old
#   # P1=0 # padding old
#   # S1=1 # stride old

#   # layer 2
#   # B1=2 # filter size old
#   # K3=10 # num filters old	
#   # Q1=0 # padding old
#   # R1=1 # stride old

#   num_solutions = 0 
#   Solutions = []

#   # for C1 in np.arange(3,N1/2,2): # filter size old
#   for N2 in np.arange(N1+1,29,2): # new img resolution
#     # for B1 in np.arange(2,N2/2): # filter size old
#       for K2 in np.arange(K1,2,-1): # new number of filters in layer 1
#         for P2 in np.arange(P1,5): # new padding size in layer 1
#           for S2 in np.arange(S1,5): # new stride in layer 1
#             ratio = np.sqrt(K1/K2)				
#             if np.int(ratio) != ratio: continue
#             C2 = ratio * C1

#             M2 = (N2 - C2 + 2*P2)  / S2  
#             M1 = (N1 - C1 + 2*P1)  / S1
#             if M2 != M1: continue

#             # 2nd layer
#             # for Q2 in np.arange(Q1,5): # new padding size in layer 2
#             #   for R2 in np.arange(R1,5): # new stride size in layer 2
#             for Q2 in np.arange(2): # new padding size in layer 2
#               for R2 in np.arange(1,2): # new stride size in layer 2

#                 B2 = ratio * B1 
#                 if np.int(B2) != B2: continue	
#                 if (M2 - B2 + 2*Q2)  / R2  !=  (M1 - B1 + 2*Q1)  / R1: continue
#                 M3 = (M2 - B2 + 2*Q2)  / R2 

#                 if B2 > M2/2: continue								

#                 # print(f'found a solution {C1}, {B1}, {N2}, {K2}, {P2}, {S1}, {B2}, {Q2}, {R2}')

#                 # print(f'1st layer old: inp res: {N1}, filter size: {C1}, num filters: {K1}, out res: {M1}, stride: {S1}, pad: {P1}')
#                 # print(f'1st layer new: inp res: {N2}, filter size: {C2}, num filters: {K2}, out res: {M2}, stride: {S2}, pad: {P2}')
#                 # print(f'2nd layer old: inp res: {M1}, filter size: {B1}, out res: {M3}, stride: {R1}, pad: {Q1}')
#                 # print(f'2nd layer new: inp res: {M1}, filter size: {B2}, out res: {M3}, stride: {R2}, pad: {Q2}\n')
#                 params_old = (K1 * C1**2 * 3) + (K3 * B1**2 * K1) 
#                 params_new = (K2 * C2**2 * 3) + (K3 * B2**2 * K2) 

#                 assert params_old==params_new, False
#                 # print(f'PARAMs old: {params_old}, PARAMs new: {params_new}\n')

#                 num_solutions += 1
#                 Solutions.append({'im_res_orig':N1, 'im_res_new':N2, 'layer1_old':[C1, K1, S1, P1], 'layer2_old':[B1, K3, R1, Q1], 'layer1':[C2, K2, S2, P2], 'layer2':[B2, K3, R2, Q2]})

#   # print(f'num solutions: {num_solutions}')
#   return Solutions



  

# def find_res_fixed_params_pool():
# 	'''
# 		Keeping the number of parameters the same using a pooling layer
# 		Approach II in the paper
# 	'''
# 	C1=3 # filter size old
# 	K1=100  # num filters old
# 	N1=20 # orig image size
# 	P1=0 # padding old
# 	S1=1 # stride old

# 	num_solutions = 0
# 	for C1 in np.arange(3,N1/2,2): # filter size old
# 		M1 = (N1 - C1 + 2*P1) / S1
# 		for N2 in np.arange(N1+1,2*N1,2):
# 			for F in np.arange(3,5):
# 				for P in np.arange(3):
# 					for S in np.arange(2,5):
# 						W1 = (N2 - C1 + 2*P1) / S1
# 						M2 = (W1 - F + 2*P)  / S

# 						if M1 != M2: continue

# 						print(f'1st layer old: inp res: {N1}, filter size: {C1}, num filters: {K1}, out res: {M1}, stride: {S1}, pad: {P1}')
# 						print(f'1st layer new: inp res: {N2}, filter size: {C1}, num filters: {K1}, out res: {M1}, stride: {S1}, pad: {P1}')
# 						print(f'pooling layer: inp res: {M1}, filter size: {F},  out res: {M2}, stride: {S}, pad: {P}')
# 						params_old = (K1 * C1**2 * 3) 
# 						params_new = (K1 * C1**2 * 3) 
# 						print(f'PARAMs old: {params_old}, PARAMs new: {params_new}\n')

# 						num_solutions += 1

# 	print(f'num solutions: {num_solutions}')











def find_res_fixed_flops():
	'''
		Keeping FLOPS the same
		Approach III in the paper
	'''

	C1=3 # filter size old
	N1=10 # orig image size
	P1=0 # padding old
	S1=1 # stride old
	Z1=10  # num filters old

	# # layer 2
	B1=2 # kernel size old
	Q1=0 # padding old
	R1=1 # stride old

	# # layer 3
	Z3 = 10 # num filters old

	num_solutions = 0

	for Z1 in np.arange(10):
		for C1 in np.arange(2,N1/2,1): # filter size old
			M1 = (N1 - C1 + 2*P1)/S1 # res next layer	
			for N2 in np.arange(N1+1,2*N1,1):
				for C2 in np.arange(C1+1,N2/2): # filter size old		
					for Z2 in np.arange(Z1-1,2,-1):
						if (C2**2) * Z2 != (C1**2) * Z1: continue
						# for C3 in np.arange(2,M1/2): # filter size second conv layer		 
						for B2 in np.arange(2,M1/2): # filter size second conv layer		 
							if B1 * C2 != B2 * C1: continue
				
							# 2nd layer
							for Q2 in np.arange(Q1,5):
								for R2 in np.arange(R1,5):
									if (M1 - B1 + 2*Q2)  / R2  !=  (M1 - B1 + 2*Q1)  / R1: continue
									M3 = int((M1 - B1 + 2*Q2)  / R2 + 1)

									FLOPS_old = (2*M1**2 * 3 * C1**2 * Z1) + (2*M3**2 * Z1 * B1**2 * Z3) 
									FLOPS_new = (2*M1**2 * 3 * C2**2 * Z2) + (2*M3**2 * Z2 * B2**2 * Z3) 
									if 	FLOPS_old == FLOPS_new:
										print(f'1st layer old: inp res: {N1}, filter size: {C1}, num filters: {Z1}, out res: {M1}, stride: {S1}, pad: {P1}')
										print(f'1st layer new: inp res: {N2}, filter size: {C2}, num filters: {Z2}, out res: {M1}, stride: {S1}, pad: {P1}')
										print(f'2nd layer old: inp res: {M1}, filter size: {B1}, out res: {M3}, stride: {Q1}, pad: {R1}')
										print(f'2nd layer new: inp res: {M1}, filter size: {B2}, out res: {M3}, stride: {Q2}, pad: {R2}')
										print(f'FLOPS old: {FLOPS_old}, FLOPS new: {FLOPS_new}\n')

										num_solutions += 1

	print(f'num solutions: {num_solutions}')




if __name__ == "__main__":
	# sol_3 = find_res_fixed_params()
	# find_res_fixed_params_pool()
	find_res_fixed_flops()








	# N1=20 # orig image size

	# # layer 1
	# C1=3 # filter size old
	# K1=100  # num filters old
	# P1=0 # padding old
	# S1=1 # stride old

	# # layer 2
	# B1=2 # filter size old
	# K3=100 # num filters old	
	# Q1=0 # padding old
	# R1=1 # stride old

	# num_solutions = 0
	# Solutions = []

	# for C1 in np.arange(3,N1/2,2): # filter size old
	# 	for N2 in np.arange(N1+1,2*N1,2): # new img resolution
	# 		for B1 in np.arange(2,N2/2): # filter size old
	# 			for K2 in np.arange(K1-1,2,-1): # new number of filters in layer 1
	# 				for P2 in np.arange(P1,10): # new padding size in layer 1
	# 					for S2 in np.arange(S1,5): # new stride in layer 1
	# 						ratio = np.sqrt(K1/K2)				
	# 						if np.int(ratio) != ratio: continue
	# 						C2 = ratio * C1

	# 						M2 = (N2 - C2 + 2*P2)  / S2  
	# 						M1 = (N1 - C1 + 2*P1)  / S1
	# 						if M2 != M1: continue

	# 						# 2nd layer
	# 						for Q2 in np.arange(Q1,10): # new padding size in layer 2
	# 							for R2 in np.arange(R1,5): # new stride size in layer 2
	# 								B2 = ratio * B1 
	# 								if np.int(B2) != B2: continue	
	# 								if (M2 - B2 + 2*Q2)  / R2  !=  (M1 - B1 + 2*Q1)  / R1: continue
	# 								M3 = (M2 - B2 + 2*Q2)  / R2 

	# 								if B2 > M2/2: continue								

	# 								# print(f'found a solution {C1}, {B1}, {N2}, {K2}, {P2}, {S1}, {B2}, {Q2}, {R2}')
	# 								print(f'1st layer old: inp res: {N1}, filter size: {C1}, num filters: {K1}, out res: {M1}, stride: {S1}, pad: {P1}')
	# 								print(f'1st layer new: inp res: {N2}, filter size: {C2}, num filters: {K2}, out res: {M2}, stride: {S2}, pad: {P2}')
	# 								print(f'2nd layer old: inp res: {M1}, filter size: {B1}, out res: {M3}, stride: {Q1}, pad: {R1}')
	# 								print(f'2nd layer new: inp res: {M1}, filter size: {B2}, out res: {M3}, stride: {Q2}, pad: {R2}\n')
	# 								params_old = (K1 * C1**2 * 3) + (K3 * B1**2 * K1) 
	# 								params_new = (K2 * C2**2 * 3) + (K3 * B2**2 * K2) 
	# 								print(f'PARAMs old: {params_old}, PARAMs new: {params_new}\n')

	# 								num_solutions += 1	

	# 								Solutions.append({'im_res_orig':N1, 'im_res_new':N2, 'layer1':[C2, K2, S2, P2], 'layer2':[B2, Q2, R2]})

	# print(f'num solutions: {num_solutions}')