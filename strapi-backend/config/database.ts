export default ({ env }) => ({
  connection: {
    client: 'postgres',
    connection: {
      host: env('DATABASE_HOST', '127.0.0.1'),
      port: env.int('DATABASE_PORT', 5432),
      database: env('DATABASE_NAME', 'topspot40'),
      user: env('DATABASE_USERNAME', 'your_postgres_user'),
      password: env('DATABASE_PASSWORD', 'your_postgres_password'),
      ssl: env.bool('DATABASE_SSL', false),
    },
    debug: false,
  },
});
