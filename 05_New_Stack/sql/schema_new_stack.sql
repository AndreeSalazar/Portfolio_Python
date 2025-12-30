CREATE TABLE IF NOT EXISTS train_new_stack (
  date DATE NOT NULL,
  store_nbr INTEGER NOT NULL,
  item_nbr INTEGER NOT NULL,
  unit_sales INTEGER NOT NULL,
  onpromotion BOOLEAN NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_train_new_stack_date ON train_new_stack(date);
CREATE INDEX IF NOT EXISTS idx_train_new_stack_store ON train_new_stack(store_nbr);
CREATE INDEX IF NOT EXISTS idx_train_new_stack_item ON train_new_stack(item_nbr);
