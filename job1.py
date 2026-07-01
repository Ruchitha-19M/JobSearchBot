if __name__ == "__main__":
    hours_since_last = get_last_run_hours()
    jobs_df = get_jobs(hours_since_last)
    save_to_excel(jobs_df)
    save_current_run_time()
