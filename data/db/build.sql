CREATE TABLE IF NOT EXISTS exp (
    userID integer PRIMARY KEY,
    socialCredit integer DEFAULT 0,
    socialCreditLock text DEFAULT CURRENT_TIMESTAMP
)