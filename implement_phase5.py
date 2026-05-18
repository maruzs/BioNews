import re

with open('src/database/manager.py', 'r', encoding='utf-8') as f:
    manager_content = f.read()

new_methods = '''
    def update_category_last_update(self, category_slug, timestamp):
        """Update global last_updated_at for a category."""
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS category_last_updates (
                    category_slug VARCHAR(255) PRIMARY KEY,
                    last_updated_at TIMESTAMP NOT NULL
                )
            """)
            cursor.execute("""
                INSERT INTO category_last_updates (category_slug, last_updated_at)
                VALUES (%s, %s)
                ON CONFLICT (category_slug) DO UPDATE 
                SET last_updated_at = EXCLUDED.last_updated_at
            """, (category_slug, timestamp))
            conn.commit()

    def check_category_has_new(self, user_id, category_slug):
        """Compare user's last_exit_at with global last_updated_at."""
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor()
            
            # Get global last update
            cursor.execute("""
                SELECT last_updated_at FROM category_last_updates 
                WHERE category_slug = %s
            """, (category_slug,))
            global_row = cursor.fetchone()
            if not global_row:
                return False
                
            # Get user's last exit
            cursor.execute("""
                SELECT last_exit_at FROM user_category_views 
                WHERE user_id = %s AND category_slug = %s
            """, (user_id, category_slug))
            user_row = cursor.fetchone()
            
            if not user_row:
                return True
                
            return global_row[0] > user_row[0]
'''

manager_content += new_methods

with open('src/database/manager.py', 'w', encoding='utf-8') as f:
    f.write(manager_content)
print("Updated manager.py")
