def minimize_lateness(jobs, deadlines):
	'''
	Get jobs and their deadlines, return minimum lateness and selected
	jobs.

	Args:
		jobs: List of time consumption for each job.
		deadlines: List of deadlines for each job.

	Return:
		scheduled_jobs(list): List of indexes of scheduled jobs
		min_max_lateness(int): int of the minimized maximum lateness
	'''
	n = len(jobs)
	jobs_init = []
	for i in range(n):
		jobs_init.append((i, jobs[i], deadlines[i]))

	jobs_sorted = sorted(jobs_init, key=lambda x:x[2])
	scheduled_jobs = [job[0] for job in jobs_sorted]
	
	time_cost = 0
	min_max_lateness = 0
	for job in jobs_sorted:
		time_cost += job[1]
		lateness = time_cost - job[2]
		min_max_lateness = max(min_max_lateness, lateness)

	return	scheduled_jobs, min_max_lateness


if __name__ == "__main__":
	print(minimize_lateness([3,2,1,4,3,2],[6,8,9,9,14,15]))
	print(minimize_lateness([1,2,3,4,3,2],[9,8,6,9,14,15]))

