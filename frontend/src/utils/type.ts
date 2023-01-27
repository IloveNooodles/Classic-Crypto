const key = ["Text", "Number"] as const;
type availableKeyType = typeof key[number];

export type { availableKeyType };
